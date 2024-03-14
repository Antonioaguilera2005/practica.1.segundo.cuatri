class Logger:
    def __init__(self):
        self.log_file = open("log.txt", "w")
        self.log_count = 0
        self.log("--Start log--")

    def log(self, message):
        self.log_file.write(message + "\n")
        self.log_count += 1

    def __del__(self):
        self.log("--End log: {} log(s)--".format(self.log_count))
        self.log_file.close()

class Test:
    def __init__(self):
        self.logger = Logger()

    def llamada(self, message):
        self.logger.log(message + "\n")

# Uso del código
test = Test()
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada("{}a llamada".format(i))


del test
