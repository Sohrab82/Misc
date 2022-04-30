import matplotlib.pyplot as plt

fig, axe = plt.subplots()
# create some curves
for i in range(4):
    # Giving unique ids to each data member
    axe.plot([i*1.5,i*2,i*3,i*4], '-o', gid=i)

annot = axe.annotate("", xy=(0,0), xytext=(20,20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)


def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))),
                           " ".join([names[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


def on_plot_hover(event):
    # Iterating over each data member plotted
    for curve in axe.get_lines():
        # Searching which data member corresponds to current mouse position

        cont, ind = curve.contains(event)
        if cont:
            pos = ind["ind"][0]
            print('curve:', curve.get_gid(), ', ', pos)

fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)
plt.show()