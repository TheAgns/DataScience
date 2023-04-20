import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_heatmap(df):
    salaries = df[[2020, 2021, 2022]]
    sns.heatmap(data=salaries, cmap='coolwarm')
    plt.title('Salary Comparison for Different Companies')
    plt.xlabel('Year')
    plt.ylabel('Company')
    plt.show()
    

def generate_wordcloud(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        
    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)

    plt.show()
    
def generate_wordcloud_image(self, filename):
    with open(filename, 'r') as f:
        text = f.read()

    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)

    plt.show()
