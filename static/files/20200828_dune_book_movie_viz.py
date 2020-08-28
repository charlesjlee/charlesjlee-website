# TODO: add hover-over (by not using shapes?)
# TODO: remove code duplication
# TODO: make interactive
# TODO: add Dune 2020 datapoints
# TODO: adjust colors
# https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
# https://www.color-hex.com/color/87cefa
# TODO: build legend properly (by using legend groupings per trace?)

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default = 'svg'
# pio.renderers.default = 'browser'

WIDTH = 100 # total width of timeline
HEIGHT = 0.3 # height of timeline boxes
X,Y = 10,3 # off-sets
SPACE = 2 # distance between timelines

def timeline_box(L, R, scene, Y=Y):
    if pd.isnull(scene) or scene not in seen:
        return dict(
            type='path',
            path=f'M {X+L},{Y-HEIGHT/2} L{X+L},{Y+HEIGHT/2} L{X+R},{Y+HEIGHT/2} L{X+R},{Y-HEIGHT/2} Z',
            fillcolor='rgba(205,92,92,0.6)', # indianred
            line_color='crimson',
            layer='above',
        )
    elif scene != 'irulan':
        return dict(
            type='path',
            path=f'M {X+L},{Y-HEIGHT/2} L{X+L},{Y+HEIGHT/2} L{X+R},{Y+HEIGHT/2} L{X+R},{Y-HEIGHT/2} Z',
            fillcolor='rgba(175,238,238,0.6)', # PaleTurquoise
            line_color='LightSeaGreen',
            layer='below',
        )
    else:
        # Irulan subplot
        return dict(
            type='path',
            path=f'M {X+L},{Y-HEIGHT/2} L{X+L},{Y+HEIGHT/2} L{X+R},{Y+HEIGHT/2} L{X+R},{Y-HEIGHT/2} Z',
            fillcolor='rgba(240,230,140,0.6)', # khaki
            line_color='goldenrod',
            layer='above',
        )

def scene_box_2000(start_book, end_book, start_movie, end_movie, Y_diff):
    return dict(
        type='path',
        path=f'M {X+start_book},{Y+HEIGHT/2} L{X+start_movie},{Y+Y_diff-HEIGHT/2} L{X+end_movie},{Y+Y_diff-HEIGHT/2} L{X+end_book},{Y+HEIGHT/2} Z',
        fillcolor='rgba(221,160,221,0.6)', # plum
        line_color='mediumorchid',
    )

def scene_box_1984(start_book, end_book, start_movie, end_movie, Y_diff):
    return dict(
        type='path',
        path=f'M {X+start_book},{Y-HEIGHT/2} L{X+start_movie},{Y+Y_diff+HEIGHT/2} L{X+end_movie},{Y+Y_diff+HEIGHT/2} L{X+end_book},{Y-HEIGHT/2} Z',        
        fillcolor='rgba(221,160,221,0.6)', # plum
        line_color='mediumorchid',
    )

# import book data
df_book = pd.read_csv(r'https://charlesjlee.com/files/20200828_dune_book_movie_viz_book.csv', dtype={'Part': object, 'EpigraphNumber': object})
df_book['Scene'] = df_book['Part'] + '.' + df_book['EpigraphNumber']
df_book['length'] = df_book['PageEnd'] - df_book['PageStart']
df_book['length_scaled'] = df_book['length'] / sum(df_book['length']) * WIDTH
df_book['end'] = df_book['length_scaled'].cumsum()
df_book['start'] = df_book['end'].shift(periods=1, fill_value=0)
df_book = df_book[['Scene','start','end']]

# import 1984 movie data
df_1984 = pd.read_csv(r'https://charlesjlee.com/files/20200828_dune_book_movie_viz_1984.csv', parse_dates=['Start', 'End'])
df_1984['length'] = (df_1984['End'] - df_1984['Start']).dt.total_seconds()
df_1984['length_scaled'] = df_1984['length'] / sum(df_1984['length']) * WIDTH
df_1984['end'] = df_1984['length_scaled'].cumsum()
df_1984['start'] = df_1984['end'].shift(periods=1, fill_value=0)
df_1984 = df_1984[['Scene','start','end']]

# import 2000 movie data
df_2000p1 = pd.read_csv(r'https://charlesjlee.com/files/20200828_dune_book_movie_viz_2000p1.csv', parse_dates=['Start', 'End'])
df_2000p2 = pd.read_csv(r'https://charlesjlee.com/files/20200828_dune_book_movie_viz_2000p2.csv', parse_dates=['Start', 'End'])
df_2000p3 = pd.read_csv(r'https://charlesjlee.com/files/20200828_dune_book_movie_viz_2000p3.csv', parse_dates=['Start', 'End'])
df_2000 = pd.concat([df_2000p1, df_2000p2, df_2000p3])
df_2000['length'] = (df_2000['End'] - df_2000['Start']).dt.total_seconds()
df_2000['length_scaled'] = df_2000['length'] / sum(df_2000['length']) * WIDTH
df_2000['end'] = df_2000['length_scaled'].cumsum()
df_2000['start'] = df_2000['end'].shift(periods=1, fill_value=0)
df_2000 = df_2000[['Scene','start','end']]

# construct timeline boxes (sort for layering)
seen = set(df_1984.Scene) | set(df_2000.Scene)

box_book = [timeline_box(a,b,c) for a,b,c in zip(df_book['start'], df_book['end'], df_book['Scene'])]
box_1984 = [timeline_box(a,b,c,Y=Y-SPACE) for a,b,c in zip(df_1984['start'], df_1984['end'], df_1984['Scene'])]

df_sorted = df_2000.sort_values(by='Scene', na_position='first')
box_2000 = [timeline_box(a,b,c,Y=Y+SPACE) for a,b,c in zip(df_sorted['start'], df_sorted['end'], df_sorted['Scene'])]

# break multi-matches into multiple rows
# (only applies to row 34 in 1984 and row 12 in 2000)
df_1984 = df_1984.assign(Scene=df_1984['Scene'].str.split('+')).explode('Scene')
df_2000 = df_2000.assign(Scene=df_2000['Scene'].str.split('+')).explode('Scene')

# construct matched scene boxes
df_book_1984 = df_book.join(df_1984.set_index('Scene'), on='Scene', lsuffix='_book', rsuffix='_movie')
df_book_2000 = df_book.join(df_2000.set_index('Scene'), on='Scene', lsuffix='_book', rsuffix='_movie')

box_book_1984 = [
    scene_box_1984(a,b,c,d,-SPACE)
    for a,b,c,d
    in zip(df_book_1984['start_book'], df_book_1984['end_book'], df_book_1984['start_movie'], df_book_1984['end_movie'])
]
box_book_2000 = [
    scene_box_2000(a,b,c,d,SPACE)
    for a,b,c,d
    in zip(df_book_2000['start_book'], df_book_2000['end_book'], df_book_2000['start_movie'], df_book_2000['end_movie'])
]

fig = go.Figure()

# scatter trace of timeline labels
fig.add_trace(go.Scatter(
    x=3*[X-1] + 3*[X+WIDTH+6],
    y=[Y, Y-SPACE, Y+SPACE, Y, Y-SPACE, Y+SPACE],
    text=["<b>Book</b>", "<b>1984 movie</b>","<b>2000 mini-series</b>", "<b>489 pages</b>", "<b>2h 12min</b>", "<b>4h 34min</b>"],
    mode="text",
    textposition='middle left',
    showlegend=False,
))

# scatter trace of part labels
fig.add_trace(go.Scatter(
    x=[
       X+(df_book.set_index('Scene').loc['1.22']['end']-df_book.set_index('Scene').loc['1.1']['start'])/2,
       X+(df_book.set_index('Scene').loc['2.15']['end']-df_book.set_index('Scene').loc['2.1']['start'])/2 + df_book.set_index('Scene').loc['1.22']['end'],
       X+(df_book.set_index('Scene').loc['3.11']['end']-df_book.set_index('Scene').loc['3.1']['start'])/2 + df_book.set_index('Scene').loc['2.15']['end'],
    ],
    y=3*[Y+SPACE+HEIGHT+0.4],
    text=["<b>Part I</b>", "<b>Part II</b>", "<b>Part III</b>"],
    mode="text",
    textposition='middle center',
    showlegend=False,
))

# off-screen scatter trace just for the legend
df = pd.DataFrame({'label': ['Matching scene', 'Non-matching scene', 'Irulan subplot'],
                    'x': 3*[-1e6],
                    'y': 3*[-1e6]})
color = {
    'Matching scene': 'LightSeaGreen',
    'Non-matching scene': 'crimson',
    'Irulan subplot': 'goldenrod',
}

for lbl in df['label'].unique():
    dfp = df[df['label']==lbl]
    fig.add_traces(go.Scatter(
        x=dfp['x'],
        y=dfp['y'],
        mode='markers',
        name=lbl,
        marker = dict(color=color[lbl], size=12),
    ))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    x=1,
    y=1.02,
    xanchor="right",
))

# update axes properties
fig.update_xaxes(
    range=[0, WIDTH + 2*X-3],
    visible=False,
)

fig.update_yaxes(
    range=[0, 3*SPACE],
    visible=False,
)

vertical_lines = [
    dict(
        type='line',
        yref='paper',
        y0=0,
        y1=1,
        xref='x',
        x0=X+df_book.set_index('Scene').loc['1.22']['end'],
        x1=X+df_book.set_index('Scene').loc['1.22']['end'],
        line=dict(
            color="gray",
            width=2,
            dash="dot",
        ),
    ),
    dict(
        type='line',
        yref='paper',
        y0=0,
        y1=1,
        xref='x',
        x0=X+df_book.set_index('Scene').loc['2.15']['end'],
        x1=X+df_book.set_index('Scene').loc['2.15']['end'],
        line=dict(
            color="gray",
            width=2,
            dash="dot",
        ),
    ),
]

def annotate(x, y, ax, ay, text):
    return dict(
        xref='paper',
        yref='paper',
        arrowhead=6,
        arrowcolor='black',
        ayref='pixel',
        
        x=x,
        y=y,
        ax=ax,
        ay=ay,
        text=text,
    )

# add shapes
fig.update_layout(
    shapes=box_book + box_1984 + box_2000 + box_book_1984 + box_book_2000 + vertical_lines,
    plot_bgcolor='lightgray',
    title={
        "text":"Scene matchings between Dune book, 1984 movie, 2000 mini-series",
        "font_size":20,
        },
)

fig.show()
fig.write_image("fig1.svg", width=1800, height=600)