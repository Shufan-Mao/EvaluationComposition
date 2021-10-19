import random
import pandas as pd


instruments = ['a','b','c']
num_phrase = 10

test = True

def generate_data(): # generate semantic relatedness dataframe(pandas), and phrase/instrument/location information
    phrase_list = []
    column_names = ['Phrase', 'Phrase Type'] + instruments
    semantic_relatedness_dataframe = pd.DataFrame(columns=column_names)
    phrase_instrument_type = pd.DataFrame(columns=column_names)

    for i in range(num_phrase):
        phrase = str((str(i), str(num_phrase-i)))
        phrase_list.append(phrase)
        phrase_type = random.choice(['control','experiment','novel','verb'])
        append_row_semantics = {'Phrase':phrase, 'Phrase Type':phrase_type}
        append_row_type = {'Phrase':phrase, 'Phrase Type':phrase_type}
        expected_instrument = random.choice(instruments)
        for instrument in instruments:
            if instrument == expected_instrument:
                instrument_type = 'expected'
            else:
                instrument_type = random.choice(['related','unrelated'])
            append_row_semantics[instrument] = random.uniform(0,1)
            append_row_type[instrument] = instrument_type
        phrase_instrument_type = phrase_instrument_type.append(append_row_type,ignore_index=True)
        semantic_relatedness_dataframe = semantic_relatedness_dataframe.append(append_row_semantics, ignore_index=True)

    return phrase_instrument_type, semantic_relatedness_dataframe



def get_data():
    if test:
        generate_data()
    else:
        pass


def main():
    phrase_instrument_type, semantic_relatedness = generate_data()
    print(semantic_relatedness)
    print(phrase_instrument_type)



main()
