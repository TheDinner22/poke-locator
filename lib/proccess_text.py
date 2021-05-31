# dependencies
import os, sys, pytesseract, re

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

if __name__ == '__main__':
    from config import pytesseract_location
    from config import pokemon_list
else:
    from lib.config import pytesseract_location
    from lib.config import pokemon_list

# tell pytesseract where to look
pytesseract.pytesseract.tesseract_cmd = pytesseract_location

class Text_Processor():
    def __init__(self, text_from_image):
        self.origonal_text = text_from_image
        self.pokemon_list = pokemon_list #TODO i may need to be an arg when name != main
        self.pokemon_spellings = ['pokénon','pokenon','pokemon','pokémon','okénon','okenon','okemon','okémon']
        self.pokemon_spellings_trimmed = ['okénon','okenon','okemon','okémon'] 
        self.pokemon_spawned = False

    def proccess_text(self):
        # make sure self.pokemon_spawned = false
        self.pokemon_spawned = False
        flag1 = False

        # see if any of the acceptable spellings of pokemon are present
        for spelling in self.pokemon_spellings:
            if self.origonal_text.find(spelling) != -1:
                flag1 = True
        
        # if there was a pokemon spawned see if it was a ledgendary
        if flag1:
            # find all instances of the work pokemon
            poke_occurrences = []
            for spelling in self.pokemon_spellings_trimmed:
                temp_list = re.findall(spelling, self.origonal_text)
                for occurrence in temp_list:
                    poke_occurrences.append(occurrence)
            
            # loop through every occurrence and look 30 characters ahead to see if a pokemon is mentioned
            # then remove the occurrence
            trimmed_string = self.origonal_text
            for occurrence in poke_occurrences:
                if trimmed_string.find(occurrence) != -1:
                    start_i = trimmed_string.find(occurrence)
                    end_i = start_i + 30 if start_i + 30 < len(trimmed_string)-1 else len(trimmed_string)-1
                    spliced_string = trimmed_string[start_i:end_i]
                    for name in self.pokemon_list:
                        if name in spliced_string:
                            self.pokemon_spawned = True
                            return True
        return self.pokemon_spawned
                





if __name__ == "__main__":
    text = '& Snorlaxa : .ar Lvl: 40 HP: 134/178ag, HServinea 2 :ay Lvl: 24 HP: 69/69  & EmolgaLvl: 36 HP: 89/89TyphlosionLvl: 38 HP: 108/108Laprashe a(Debuagl: Hitboxes: shownnutsdoin our Discord https//discordgg/PokecentralPokénon Heatran MesaPro GlazeFrost > GLAlzz_ Heatran despaunex xdYour party is full, Deino was sent to your PC!Pro GlazeFrost > That was fastAlzz_ YerPro Tieger_ > Pog i♀'.strip().lower()
    text_processor = Text_Processor(text)
    my_bool = text_processor.proccess_text()
    print(text_processor.pokemon_spawned)