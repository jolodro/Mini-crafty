import os
import subprocess
import psutil
import time
import threading


class MinecraftServer:

    def __init__(self, server_path, jar, ram_mb, port):
        self.server_path = server_path
        self.jar = jar
        self.ram_mb = ram_mb
        self.port = port
        self.process = None
        self.pid = None
        self.start_time = None
        self.logs = []
    
    def _read_output(self):
        for line in self.process.stdout:
            self.logs.append(line.rstrip())
            if len(self.logs) > 500:
                self.logs.pop(0)

    def is_running(self):
        if self.pid is None:
            return False
        return psutil.pid_exists(self.pid)

    def start(self):
        if self.is_running():
            return False

        cmd = [
            "java",
            f"-Xmx{self.ram_mb}M",
            "-jar",
            self.jar,
            "--port",
            str(self.port),
            "nogui"
        ]

        self.process = subprocess.Popen(
            cmd,
            cwd=self.server_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        time.sleep(1)

        self.pid = self.process.pid
        self.start_time = time.time()
        threading.Thread(target=self._read_output, daemon=True).start()
        return True

    def stop(self):
        if not self.is_running():
            return False

        p = psutil.Process(self.pid)
        p.terminate()
        p.wait(timeout=25)

        self.pid = None
        self.process = None
        return True

    def status(self):
        return {
            "running": self.is_running(),
            "pid": self.pid,
            "port": self.port,
            "ram_mb": self.ram_mb,
            "uptime": int(time.time() - self.start_time) if self.start_time else 0
        }

    def send_command(self, cmd):
        if self.process and self.is_running():
            self.process.stdin.write(cmd + "\n")
            self.process.stdin.flush()