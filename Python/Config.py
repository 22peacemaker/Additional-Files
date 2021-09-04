import os

class Config:

    def __init__(self, path: str = "default"):
        if path == "default":
            self.path = "/home/carAI/default.cfg"
        else:
            self.path = path

        self.conf = {}
        self.read()
        print(self.conf)

    def __getitem__(self, key: str):
        return self.conf[key]

    def __setitem__(self, key, value):
        self.write(key, value)
        self.conf[key] = value
        print(self.conf)

    def read(self) -> None:

        with open(self.path) as f:
            a = f.readlines()
            for i in range(len(a)):
                a[i] = a[i].replace("\n", "")
        self.parse_config(a)

    def parse_config(self, cfg_raw: list) -> None:
        for c in range(len(cfg_raw)):
            a = cfg_raw[c].split("=", maxsplit=1)
            self.conf[a[0]] = a[1]
        
    def write(self, key: str, value: str) -> None:

        with open(self.path, "a") as f:
            f.write("\n")
            f.write(key + "=" + value)

    def change_config(self, key: str, value: str) -> bool:
        changed = False
        pass
        #Todo implement

if __name__ == "__main__":
    c = Config(os.getcwd() + "\\default.cfg")