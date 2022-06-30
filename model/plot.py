#plot each attribute
import seaborn as sns
import matplotlib.pyplot as plt


def _plotall(data, ticker):
    df_plot = data[ticker].copy()
    del (df_plot['volume'])
    list_length = df_plot.shape[1]
    ncols = 2
    nrows = int(round(list_length / ncols, 0))
    print(ticker)
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, sharex=True, figsize=(14, 7))
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    for i in range(0, list_length):
            ax = plt.subplot(nrows,ncols,i+1)
            sns.lineplot(data = df_plot.iloc[:, i], ax=ax)
            ax.set_title(df_plot.columns[i])
            ax.tick_params(axis="x", rotation=30, labelsize=10, length=0)
    fig.tight_layout()
    plt.show()