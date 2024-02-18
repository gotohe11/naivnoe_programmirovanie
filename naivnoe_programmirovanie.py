import requests
project_name=input('input owner/repo (for example, "NixOS/nixpkgs"):')
#project_name='shobrook/rebound'    # one page project
#project_name='s0md3v/Photon'    # two pages project
#project_name='karpathy/neuraltalk2'    # 5 pages project
#project_name='3b1b/manim'    # many pages project
base_url=f'https://api.github.com/repos/{project_name}/issues'
response = requests.get(base_url)
#print(response.status_code)

def make_issues_list(url):
    response = requests.get(url)
    issue_list=[]
    for item in response.json():
        if not 'pull_request' in item.keys():
            issue_list.append(item['title'])
    return issue_list

print('List issues in a repository (only open issues will be listed):')

total_list=[]
if response.status_code != 200 :
    print("ooops! let's try one more time")
if response.status_code == 200 and not 'link' in response.headers:
    lst = make_issues_list(base_url)
    total_list.extend(lst)
if response.status_code == 200 and 'link' in response.headers:
    counter=1
    temp_list=['ololo pysch pysch']
    while len(temp_list)!=0:
        add_url = f'{base_url}?page={counter}'
        temp_list = make_issues_list(add_url)
        total_list.extend(temp_list)
        counter+=1


for i in range(len(total_list)):
    print(f'{i+1}. {total_list[i]}', sep='\n')