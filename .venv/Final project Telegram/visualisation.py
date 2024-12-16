from pandas import DataFrame, read_csv
import pandas
from matplotlib import pyplot as plt

class Graphic:
    def __init__(self, path="график семантического тега.png", csv_path = "output.csv"):
        self.path = path
        self.csv_path = csv_path

    def create_graphic(self):
        frame = read_csv(self.csv_path)

        semantic_map = {'Negative': -1, 'Neutral': 0, 'Positive': 1}

        frame['семантический тег'] = frame['семантический тег'].map(semantic_map)

        frame['число'] = pandas.to_datetime(frame['число'], format='%d.%m.%Y')


        daily_sum = frame.groupby('число')['семантический тег'].sum().reset_index()  # use reset_index to convert the date into a column


        full_of_date = pandas.date_range(start=daily_sum['число'].min(),
                                        end=daily_sum['число'].max())
        daily_sum = daily_sum.set_index('число').reindex(full_of_date,
                                                                          fill_value=0).reset_index()
        daily_sum.columns = ['Число', 'Общее значение семантического тега']


        plt.figure(figsize=(15, 5))
        plt.plot(daily_sum['Число'], daily_sum['Общее значение семантического тега'], marker='o',color="red")
        plt.title('Таймлайн общего значения семантического тега',fontweight = "bold")
        plt.xlabel('Число',fontweight = "bold")
        plt.ylabel('Общее значение семантического тега',fontweight = "bold")
        plt.xticks(daily_sum['Число'], rotation=45)
        plt.tight_layout()
        return plt


graphic_creator = Graphic()
timeline = graphic_creator.create_graphic()
timeline.savefig(graphic_creator.path)