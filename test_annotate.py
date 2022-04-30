import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)

# (x, y) value pairs
x = np.random.rand(15)
y = np.random.rand(15)
# annotations for each point
names = np.array(list("ABCDEFGHIJKLMNO"))
# random color
c = np.random.randint(1, 5, size=15)

# scatter plot properties
norm = plt.Normalize(1, 4)
cmap = plt.cm.RdYlGn
fig, ax = plt.subplots()
sc = plt.scatter(x, y, c=c, s=100, cmap=cmap, norm=norm)

# create an annotation object for the axes and set it to invisible
annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)


def update_annot(ind):
    # function to update the annotation object position, label, color, and etc
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
                           " ".join([names[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    # this function runs on motion_notify_event (mouse events)
    # and updates/shows the annotation object by calling update_annot
    # function, or hide the annotation
    vis = annot.get_visible()
    if event.inaxes == ax:
        # if mouse event has happened inside ax
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


# attach "hover" function to motion_notify_event
fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
