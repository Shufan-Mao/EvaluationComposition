import phrasal_task as pt
import pandas as pd
import matplotlib.pyplot as plt

num_model = 6

class Model_result():

    def __init__(self, name, adjunct_type, semantic_relatedness, phrase_instrument_type):
        self.model_name = name
        self.adjunct_type = adjunct_type # instrument or location

        self.phrase_instrument_type = phrase_instrument_type
        self.semantic_relatedness = semantic_relatedness
        self.phrase_list = semantic_relatedness['Phrase'].tolist()
        self.instrument_list = list(self.semantic_relatedness)[2:]
        self.sr_rankings = pt.get_ranking(self.semantic_relatedness)



    def get_mean_rankings(self,phrase_type):
        df_sr = self.sr_rankings[self.sr_rankings['Phrase Type'] == phrase_type]
        df_type = self.phrase_instrument_type[self.phrase_instrument_type['Phrase Type'] == phrase_type]
        sub_phrase_list = df_sr['Phrase'].to_list()

        ranking_dict = {'Phrase':sub_phrase_list,'expected':[],'related':[],'unrelated':[]}

        for phrase in sub_phrase_list:
            expected_ranking = 0

            related_ranking = 0
            related_num = 0

            unrelated_ranking = 0
            unrelated_num = 0

            for instrument in self.instrument_list:
                instrument_type = df_type.loc[df_type['Phrase'] == phrase, instrument].tolist()[0]
                ranking = df_sr.loc[df_sr['Phrase'] == phrase, instrument].tolist()[0]

                if instrument_type == 'expected':
                    expected_ranking = expected_ranking + ranking
                elif instrument_type == 'related':
                    related_ranking = related_ranking + ranking
                    related_num = related_num + 1
                else:
                    unrelated_ranking = unrelated_ranking + ranking
                    unrelated_num = unrelated_num + 1

            related_ranking = related_ranking/max(related_num,1)
            unrelated_ranking = unrelated_ranking/max(unrelated_num,1)

            ranking_dict['expected'].append(expected_ranking)
            ranking_dict['related'].append(related_ranking)
            ranking_dict['unrelated'].append(unrelated_ranking)

        df_mean = pd.DataFrame(data=ranking_dict)

        return df_mean


def plot_expected_rankings(models, phrase_type): # plot ranking of expected instrument for all phrases
    phrase_list = []

    for model in models:
        df_model = model.get_mean_rankings(phrase_type)
        model_ranking = df_model['expected'].tolist()
        if models.index(model) == 0:
            phrase_list = df_model['Phrase'].tolist()

        plt.plot(phrase_list, model_ranking, label = model.model_name)

    plt.xticks(color='white')
    plt.legend()
    plt.show()

def plot_ranking_type(models, phrase_type, fig_size): # instruments'rankings are collasped by types for each model
    num_row = fig_size[0]
    num_col = fig_size[1]
    fig, axs = plt.subplots(num_row, num_col)
    instrument_type = []
    handles = None
    labels = None
    for i in range(num_row):
        for j in range(num_col):
            model = models[i*num_col + j]
            df_model = model.get_mean_rankings(phrase_type)
            if i==0 and j==0:
                instrument_type = list(df_model)[1:]
            mean_ranking = df_model[instrument_type].mean(axis=0)


            axs[i, j].bar(instrument_type, mean_ranking, color = ['red','blue','purple'])
            axs[i, j].set_title(model.model_name)
            axs[i, j].set_xticks([])

            if i+1 == num_row and j+1 == num_col:
                handles, labels = axs[i,j].get_legend_handles_labels()



    for ax in axs.flat:
        ax.set(xlabel='Instrument Type', ylabel='Average Ranking')
        ax.label_outer()


    fig.legend(handles, labels, loc='upper center')
    plt.show()


def get_models():
    model_list = []
    for i in range(num_model):
        name = 'M' + str(i)
        adjunct_type = 'instrument'
        phrase_instrument_type, semantic_relatedness = pt.generate_data()
        model_list.append(Model_result(name,adjunct_type,semantic_relatedness,phrase_instrument_type))
    return model_list


def main():
    models = get_models()
    plot_expected_rankings(models, 'control')
    plot_ranking_type(models, 'control',(2,3))


main()