from rule_generator import RuleGenerator

rg = RuleGenerator()


with open(r'config.json', 'r') as sv:
    config = json.load(sv)





if __name__ == "__main__":
    #interjections_file = "@ChatScriptInstallDir@/LIVEDATA/FRENCH/SUBSTITUTES/interjections.txt"
    #concepts_file = "@ChatScriptInstallDir@/RAWDATA/IAGOTCHI/iagotchi_concepts.top"
    #data_file = "@CMAKE_INSTALL_PREFIX@/data/base de données RENCONTRE corrigée.txt"
    qafile = "text.txt"
    rg.interjection_concepts(config['interjection'])
    rg.build_concepts(config['concepts'])
    #QA_File(data_file)
    data = rg.loaddata(qafile)
    interjections, concepts_words, words_concepts = rg.load_interjections_concepts()
    
    rg.generete_rules(data, interjections, concepts_words, words_concepts)
    
