class Patient:
    def __init__(self,p_name, p_address, p_programme):
        self.name = p_name
        self.address = p_address
        self.programme = p_programme

        def printdetails(self):
            return f"Patient name is {self.name}. address is {self.address} and programme is {self.programme}"


sabbir = Patient("Sabbir Ahamed", "222 Windshor ave, Clifton 07100", "Alesenssa")
michael = Patient("Michael Horton", "2 Clifton ave, Jackson 07100", "Tricentic")
teja = Patient("Sri Teja", "19 Blackend ave, Wayne 07100", "Zalboraf")
Prassana = Patient("Prassana Telugo", "34 Windshor ave, Manchester 07100", "Amgen first step")
Kelly = Patient("Kelly Anderson", "17 Laila ave, Brookdale 07100", "Jibi")

print(sabbir.name)
