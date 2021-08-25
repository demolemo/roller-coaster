import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load rankings data here:
steel = pd.read_csv('./Golden_Ticket_Award_Winners_Steel.csv')
wood = pd.read_csv('./Golden_Ticket_Award_Winners_Wood.csv')
roller_coaster = pd.read_csv('./roller_coasters.csv')


# write function to plot rankings over time for 1 roller coaster here:
def plot_rankings(coaster, park):
    material = roller_coaster.loc[(roller_coaster.name == coaster) &
                (roller_coaster.park == park)].material_type
    if material.item() == 'Wooden':
        df = wood
    else:
        df = steel

    df = df.loc[(df.Name == coaster) & (df.Park == park)]
    years = df['Year of Rank']
    ranking = df['Rank']

    if len(years) == 0:
        return 0
    else:
        plt.figure(figsize=(10, 8))
        ax = plt.subplot()
        plt.plot(years, ranking, marker='8')
        plt.xlabel('Years')
        plt.ylabel('Rank')
        ax.invert_yaxis()
        plt.title('{} rankings'.format(coaster))
        plt.show()

# bad func call & good func call
# plot_rankings('Goudurix', 'Parc Asterix')
# plot_rankings('El Toro', 'Six Flags Great Adventure')

# write function to plot rankings over time for 2 roller coasters here:
def double_plot_rankings(coaster_a, park_a, coaster_b, park_b):
    material_a = roller_coaster.loc[(roller_coaster.name == coaster_a) &
                (roller_coaster.park == park_a)].material_type

    material_b = roller_coaster.loc[(roller_coaster.name == coaster_b) &
                (roller_coaster.park == park_b)].material_type


    if material_a.item() == 'Wooden':
        df_a = wood
    else:
        df_a = steel

    if material_b.item() == 'Wooden':
        df_b = wood
    else:
        df_b = steel


    df_a = df_a.loc[(df_a.Name == coaster_a) & (df_a.Park == park_a)]
    df_b = df_b.loc[(df_b.Name == coaster_b) & (df_b.Park == park_b)]
    years_a = df_a['Year of Rank']
    ranking_a = df_a['Rank']
    years_b = df_b['Year of Rank']
    ranking_b = df_b['Rank']

    if len(years_a) == 0 or len(years_b) == 0:
        return 0
    else:
        plt.figure(figsize=(10, 8))
        ax = plt.subplot()
        plt.plot(years_a, ranking_a, marker='8', color='green')
        plt.plot(years_b, ranking_b, marker='s', color='red')
        plt.xlabel('Years')
        plt.ylabel('Rank')
        plt.legend([coaster_a, coaster_b])
        plt.title('{} and {} rankings'.format(coaster_a, coaster_b))
        ax.invert_yaxis()
        plt.show()


# Func check
# print(double_plot_rankings('El Toro', 'Six Flags Great Adventure', \
#                      'Boulder Dash', 'Lake Compounce'))

# write function to plot top n rankings over time here:

def top_ranked(num, material):
    if material == 'Wood':
        df = wood
    else:
        df = steel

    legend = []
    plt.figure(figsize=(10,8))
    ax = plt.subplot()
    min_rank = 100
    max_rank = 0
    for i in range(num):
        coaster = df.loc[i, 'Name']
        park = df.loc[i, 'Park']
        df_i = df.loc[(df.Name == coaster) & (df.Park == park)]
        years_i = df_i['Year of Rank']
        ranking_i = df_i['Rank']
        plt.plot(years_i, ranking_i)
        legend.append(coaster)

        min_rank_i = df_i['Rank'].min()
        max_rank_i = df_i['Rank'].max()
        if min_rank_i < min_rank:
            min_rank = min_rank_i
        if max_rank_i > max_rank:
            max_rank = max_rank_i
    plt.xlabel('Years')
    plt.ylabel('Rank')
    plt.legend(legend)
    plt.title('Top {} roller-coasters rankings'.format(num))
    ax.set_yticks(range(min_rank, max_rank))
    ax.invert_yaxis()
    plt.show()

# Func tests
# top_ranked(5, 'Wood')
# top_ranked(6, 'Steel')
# load roller coaster data here:



# write function to plot histogram of column values here:

def plot_histogram(column):
    if column == 'speed':
        bin_num = 12
        data = roller_coaster[column]
    elif column == 'height':
        bin_num = 15
        data = np.log(roller_coaster[column])
    elif column == 'length':
        bin_num = 15
        data = np.log(roller_coaster[column])

    plt.figure(figsize=(10, 8))
    ax = plt.subplot()
    if column == 'height':
        plt.hist(data, bins=bin_num, range=(0,7), color='#5B5BC1')
        plt.title('Height(log) distribution across roller-coasters')
    else:
        plt.hist(data, bins=bin_num, color='#5B5BC1')
        plt.title('{} distribution across roller-coaters'.format(column.capitalize()))
    plt.xlabel(column.capitalize())
    plt.ylabel('Number of coasters')
    plt.show()

# Test func call
# plot_histogram('height')
# plot_histogram('speed')

# write function to plot inversions by coaster at a park here:

def plot_inversions_bar():
    plt.figure(figsize=(10,8))
    ax = plt.subplot()
    grouped_by_cnt = roller_coaster.groupby(['num_inversions']).count().reset_index()
    print(grouped_by_cnt)
    plt.bar(range(13), grouped_by_cnt.name)
    ax.set_xticks(range(13))
    plt.xlabel('Number of Inversions')
    plt.ylabel('Roller Coaster count')
    plt.title('Hardest rides rating')
    ax.set_xticklabels(grouped_by_cnt.num_inversions)
    plt.show()


# Test func call
# plot_inversions_bar()

# write function to plot pie chart of operating status here:
def plot_pie():
    grouped_by_status = roller_coaster.groupby(['status']).count().reset_index()
    status_cnt = grouped_by_status[['status', 'name']].reset_index()
    status_cnt.status = status_cnt.status.apply(lambda x: x.split('.')[1:])
    status_cnt = status_cnt.sort_values('name')

    legend = []
    for list in status_cnt.status.tolist():
        string = ' '.join(list)
        legend.append(string.capitalize())

    explode = [0, 0, 0, 0, 0, 0, 0, 0, 0.2]
    plt.figure(figsize=(10,8))
    ax = plt.subplot()
    plt.pie(status_cnt.name, autopct='%1.1f%%', explode=explode, shadow=True,\
            pctdistance=1.2)
    plt.title('Roller-Coasters status distribution')
    plt.axis('equal')
    plt.legend(legend)
    plt.show()


# Pie func test
# plot_pie()

# write function to create scatter plot of any two numeric columns here:
def plot_scatter(column_a, column_b):
    plt.figure(figsize=(10, 8))
    ax = plt.subplot()
    x_scale = roller_coaster[column_a]
    y_scale = roller_coaster[column_b]

    plt.scatter(x_scale, y_scale, color='green', s=1)
    plt.xlabel(column_a.capitalize())
    plt.ylabel(column_b.capitalize())
    plt.title('{} VS {}'.format(column_a.capitalize(), column_b.capitalize()))
    plt.show()

# Plot scatter without normalizing test func
# plot_scatter('height', 'speed')
# plot_scatter('length', 'speed')
# plot_scatter('length', 'height')


def plot_bar_seattype():
    plt.figure(figsize=(10, 8))
    ax = plt.subplot()
    grouped_by_seat = roller_coaster.groupby(['seating_type']).count().reset_index()
    x_scale = grouped_by_seat.seating_type.tolist()
    y_scale = np.log(grouped_by_seat.status.tolist())
    y_labels = ['e ** ' + str(i) for i in range(9)]

    plt.bar(range(len(x_scale)), y_scale, color='#7C2C2C')
    plt.xlabel('Seating type')
    plt.ylabel('Count(logged)')
    plt.title('Seating type count (logged)')
    ax.set_xticks(range(len(x_scale)))
    ax.set_xticklabels(x_scale)
    ax.set_yticklabels(y_labels)
    plt.xticks(rotation=45)
    plt.show()



# PLot bar seating_type test
# plot_bar_seattype()















#end)
