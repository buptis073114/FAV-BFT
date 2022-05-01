import numpy as np
import matplotlib.pyplot as plt
import random


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3),
                    # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


with plt.style.context(['science', 'ieee']):
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

    data = [random.randint(0, 100) for _ in range(4)]

    colors = []
    for _ in range(int(len(data) / 2)):
        colors.append([_ / int(len(data) / 2), 0.5, 0.5])
    colors = colors + colors[::-1]

    labels = [20, 50, 100, 200]

    challengenum = [20, 50, 100, 200]
    echo_challengenum = [20, 50, 100, 200]
    valnum = [20, 50, 100, 200]
    echonum = [20, 50, 100, 200]
    readynum = [20, 50, 100, 200]
    width = 0.35
    x = np.arange(len(labels))  # the label locations

    rects1 = ax1.bar(x - width / 5, challengenum, width, color='red', label='challenge number')
    rects2 = ax1.bar(x - width / 5, echo_challengenum, width, color='blue', label='echo-challenge number')
    rects3 = ax1.bar(x - width / 5, valnum, width, color='green', label='val number')
    rects4 = ax1.bar(x - width / 5, echonum, width, color='black', label='echo number')
    rects5 = ax1.bar(x - width / 5, readynum, width, color='yello', label='ready number')

    autolabel(rects1)
    autolabel(rects2)

    ax1.set_xlabel("number of nodes")
    ax1.set_ylabel("times")

    ax1.set_title('(1) number of different phases in VoFC')

    ax1.bar([20, 50, 100, 200], [[20, 50, 100, 200], [20, 50, 100, 200], [20, 50, 100, 200], [20, 50, 100, 200]],
            color=colors, width=10)

    ax1.grid(True)

    _chatau500 = [20, 50, 100, 200]
    _chatau500time = np.array([21, 46, 172, 758])

    _chatau5000 = [20, 50, 100, 200]
    _chatau5000time = np.array([1421, 3012, 12050, 96384])

    _chatau10000 = [20, 50, 100, 200]
    _chatau10000time = np.array([5167, 10334, 41336, 330688])

    _chatau50000 = [20, 50, 100, 200]
    _chatau50000time = np.array([12618, 10334, 41336, 330688])

    _chatau100000 = [20, 50, 100, 200]
    _chatau100000time = np.array([50619, 10334, 41336, 330688])

    _chatau300000 = [20, 50, 100, 200]
    _chatau300000time = np.array([73719, 10334, 41336, 330688])

    ax2.set_xlabel("number of nodes")
    ax2.set_ylabel("consumed time(ms)")

    ax2.set_title('(2) time consumed by VoFC and RBC algorithm')
    chaline0, = ax2.plot(_chatau500, _chatau500time, label=r'RBC algorithm of HB-BFT', linestyle=':', marker='^')
    chaline1, = ax2.plot(_chatau5000, _chatau5000time, label=r'file size=5MB', linestyle='-', marker='p')
    chaline2, = ax2.plot(_chatau10000, _chatau10000time, label=r'file size=50MB', linestyle=':', marker='*')

    ax2.legend()
    ax2.legend(handles=[chaline0, chaline1, chaline2], loc="upper left")
    ax2.grid(True)

    fig.savefig('figures/fig4a1.pdf')
    fig.savefig('figures/fig4a1.jpg', dpi=300)

