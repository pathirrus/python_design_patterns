# SRP - Single Responsible Principle (Zasada jednej odpowiedzialności)

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        return "\n".join(self.entries)

    # łamiemy S
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


j = Journal()
j.add_entry("Wstałem")
j.add_entry("Ubrałem się")


# print(f"Journal entries:\n{j}")

# Nie łamiemy S
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w', encoding='utf-8')
        file.write(str(journal))
        file.close()


filename = r"journal.txt"
PersistenceManager.save_to_file(j, filename)

with open(filename, 'r', encoding='utf-8') as journal:
    print(journal.read())

# God object - antywzorzec
