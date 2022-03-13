import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt


def graphpy(file_path):
    df = pd.read_excel(file_path)
    
    # LoadFactor（座席利用率）を算出する
    # mapメソッドとformat()関数で%表記に変換する
    df['LF'] = df['旅客数'] / df['座席数']
    df['LF'] = df['LF'].map('{:.1%}'.format)

    # グラフの作成、3つのグラフを1つのファイルにまとめる
    plt.figure()

    fig, ax = plt.subplots(ncols=3, figsize=(16, 9), dpi=120)

    x = df['運航月']

    # ①運航回数の折れ線グラフ
    ax[0].plot(x, df.loc[:, '運航回数'], label='Flight')
    ax[0].set_title('Flight')
    ax[0].legend()
    ax[0].grid()
    ax[0].xaxis.set_tick_params(rotation=90)

    # ②旅客数と座席数の折れ線
    ax[1].plot(x, df.loc[:, '旅客数'], label='Pax', marker='D')
    ax[1].plot(x, df.loc[:, '座席数'], label='Seat', marker='*')
    ax[1].set_title('Pax/Seat')
    ax[1].legend()
    ax[1].grid()
    ax[1].xaxis.set_tick_params(rotation=90)

    # ③LFのヒストグラム
    sorted_df = df.sort_values('LF', ascending=True)
    sorted_data = sorted_df['LF']
    n, bins, patches= ax[2].hist(sorted_data, bins=10)
    ax[2].set_title('LF')
    ax[2].xaxis.set_tick_params(rotation=90)
    ax[2].set_ylim(0, 5)

    plt.subplots_adjust(wspace=0.2, hspace=0.6)
    plt.savefig('download/' + file_path[7:-5] + '_graph.png')
    plt.close('all')

    # ヒストグラムの度数分布表を表示してみる
    for i, num in enumerate(n):
        print('{:.1f} - {:.1f} : {}'.format(bins[i], bins[i + 1], num))


if __name__ == '__main__':
    file_path = 'sample.xlsx'
    graphpy(file_path)
    