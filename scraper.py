import json
from pprint import pprint

from bs4 import BeautifulSoup

# from https://www.reddit.com/r/RoastMe/comments/9ob1iu/i_eat_a_banana_every_day_roast_me/.mobile
with open('lucas.html', 'r') as html_file:
    html_doc = html_file.read().replace('\n', '')

soup = BeautifulSoup(html_doc, 'html.parser')


def callulate_depth(comment):
    count = 0

    parent = comment
    while True:
        parent = parent.parent.parent.parent

        if parent.name == 'hr':
            return count

        count = count + 1


def get_comments_in_list(comment_divs):
    aggregated_comments = []

    for comment in comment_divs:
        author = comment.find('a', {'class': 'author'}).text
        parrent_div_name = comment.parent.parent.parent.name  # comment>li>ul>div/hr
        score = int(comment.find('span', {'class': 'score'}).text.replace(" points", ""))
        is_sub_comment = parrent_div_name == 'div'
        comment_text = comment.find('div', {'class': 'md'}).text

        depth = 0
        if is_sub_comment:
            depth = callulate_depth(comment)

        comment_dict = {
            'author': author,
            'score': score,
            'depth': depth,
            'comment': comment_text,
            'sub_comments': []
        }

        # print(depth, author, score, comment_text)

        if depth == 0:
            aggregated_comments.append(comment_dict)
        elif depth == 1:
            parent = aggregated_comments[-1]
            parent['sub_comments'].append(comment_dict)
        elif depth == 2:
            parent = aggregated_comments[-1]
            parent2 = parent['sub_comments'][-1]
            parent2['sub_comments'].append(comment_dict)
        elif depth == 3:
            parent = aggregated_comments[-1]
            parent2 = parent['sub_comments'][-1]
            parent3 = parent2['sub_comments'][-1]
            parent3['sub_comments'].append(comment_dict)
        elif depth == 4:
            parent = aggregated_comments[-1]
            parent2 = parent['sub_comments'][-1]
            parent3 = parent2['sub_comments'][-1]
            parent4 = parent3['sub_comments'][-1]
            parent4['sub_comments'].append(comment_dict)
        elif depth == 5:
            parent = aggregated_comments[-1]
            parent2 = parent['sub_comments'][-1]
            parent3 = parent2['sub_comments'][-1]
            parent4 = parent3['sub_comments'][-1]
            parent5 = parent4['sub_comments'][-1]
            parent5['sub_comments'].append(comment_dict)
        elif depth == 6:
            parent = aggregated_comments[-1]
            parent2 = parent['sub_comments'][-1]
            parent3 = parent2['sub_comments'][-1]
            parent4 = parent3['sub_comments'][-1]
            parent5 = parent4['sub_comments'][-1]
            parent6 = parent5['sub_comments'][-1]
            parent6['sub_comments'].append(comment_dict)
        elif depth == 7:
            parent = aggregated_comments[-1]
            parent2 = parent['sub_comments'][-1]
            parent3 = parent2['sub_comments'][-1]
            parent4 = parent3['sub_comments'][-1]
            parent5 = parent4['sub_comments'][-1]
            parent6 = parent5['sub_comments'][-1]
            parent7 = parent6['sub_comments'][-1]
            parent7['sub_comments'].append(comment_dict)

    return aggregated_comments




# APPROACH 1

comment_divs = soup.find_all('div', {'class': 'comment'})

aggregated_comments = get_comments_in_list(comment_divs)

pprint(aggregated_comments)

with open('data.json', 'w') as outfile:
    json.dump(aggregated_comments, outfile)



