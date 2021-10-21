import numpy as np
import pandas as pd
import scipy.stats as ss


instruments = ['a','b','c','d','e']
num_phrase = 60 # in test version, always a multiple of num of types

test = True

def generate_data(): # generate semantic relatedness dataframe(pandas), and phrase/instrument/location information
    phrase_list = []
    types = np.random.permutation(['control','experiment','novel','verbD'])
    column_names = ['Phrase', 'Phrase Type'] + instruments
    semantic_relatedness_dataframe = pd.DataFrame(columns=column_names)
    phrase_instrument_type = pd.DataFrame(columns=column_names)

    for i in range(num_phrase):
        phrase = str((str(i), str(num_phrase-i)))
        phrase_list.append(phrase)


        phrase_type = types[i%len(types)]
        append_row_semantics = {'Phrase':phrase, 'Phrase Type':phrase_type}
        append_row_type = {'Phrase':phrase, 'Phrase Type':phrase_type}

        expected_instrument, related_instrument, unrelated_instrument = np.random.choice(instruments, 3, replace=False)
        for instrument in instruments:
            if instrument == expected_instrument:
                instrument_type = 'expected'
            elif instrument == related_instrument:
                instrument_type = 'related'
            elif instrument == unrelated_instrument:
                instrument_type = 'unrelated'
            else:
                instrument_type = np.random.choice(['related','unrelated'])
            append_row_semantics[instrument] = np.random.uniform(0,1)
            append_row_type[instrument] = instrument_type
        phrase_instrument_type = phrase_instrument_type.append(append_row_type,ignore_index=True)
        semantic_relatedness_dataframe = semantic_relatedness_dataframe.append(append_row_semantics, ignore_index=True)

    return phrase_instrument_type, semantic_relatedness_dataframe



def get_ranking(sr_dataframe): #transfer SR matrix to rankings
    phrase_list = sr_dataframe['Phrase'].tolist()
    phrase_type_list = sr_dataframe['Phrase Type'].tolist()
    column_names = list(sr_dataframe)[2:]
    sr_matrix = sr_dataframe[column_names].to_numpy()
    for i in range(len(sr_matrix)):
        sr_matrix[i] = ss.rankdata(-sr_matrix[i])

    sr_rankings = pd.DataFrame(sr_matrix,columns=column_names)
    sr_rankings.insert(0,'Phrase', phrase_list)
    sr_rankings.insert(1,'Phrase Type', phrase_type_list)

    return sr_rankings


def main():
    phrase_instrument_type, semantic_relatedness = generate_data()
    sr_rankings = get_ranking(semantic_relatedness)
    #print(semantic_relatedness)
    #print(phrase_instrument_type)
    #print(sr_rankings)



main()
