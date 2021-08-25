import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel = pd.read_csv('./Golden_Ticket_Award_Winners_Steel.csv')
wood = pd.read_csv('./Golden_Ticket_Award_Winners_Wood.csv')
roller_coaster = pd.read_csv('./roller_coasters.csv')
# print(wood.head())
# print(steel.head())
# print(roller_coaster.head())
# print(wood.info())
# print(steel.info())
# print(roller_coaster.info())




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










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
