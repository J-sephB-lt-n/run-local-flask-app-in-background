import subprocess

class BackgroundLocalHost:
    def __init__(self, app_name: str, port: int) -> None:
        self.app_name = app_name
        self.port = port
        self.process = None

    def __enter__(self) -> None:
        self.process = subprocess.Popen(
            ["flask", "--app", self.app_name, "run", "--port", str(self.port)]
        )
        print(f"hosting local flask app '{self.app_name}' on port {self.port}") 

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.process.kill()
        print(f"killed local flask app '{self.app_name}' on port {self.port}")

