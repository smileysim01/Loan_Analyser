# project: p3
# submitter: simran4
# partner: none
# hours: 20

import pandas as pd
import io
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import requests

df = pd.DataFrame([
    [0,1,0,0],
    [0,0,1,1],
    [0,0,0,1],
    [0,0,1,0],
], index=["A", "B", "C", "D"], columns=["A", "B", "C", "D"])

class GraphSearcher:
    def __init__(self):
        self.visited = set()
        self.order = []

    def go(self, node):
        raise Exception("must be overridden in sub classes -- don't change me here!")

    def dfs_search(self, node):
        # 1. clear out visited set
        self.order.clear()
        self.visited.clear()
        # 2. start recursive search by calling dfs_visit
        self.dfs_visit(node)

    def dfs_visit(self, node):
        # 1. if this node has already been visited, just `return` (no value necessary)
        if node in self.visited:
            return
        # 2. mark node as visited by adding it to the set
        self.visited.add(node)
        # 3. add this node to the end of self.order
        self.order.append(node)
        # 4. get list of node's children with this: self.go(node)
        children = self.go(node)
        # 5. in a loop, call dfs_visit on each of the children
        for child in children:
            self.dfs_visit(child)
        
    def bfs_search(self, node):
        self.order.clear()
        self.visited.clear()
        temp_queue = []
        temp_queue.append(node)
        
        while len(temp_queue) > 0:
            current_node = temp_queue.pop(0)
            
            if current_node in self.visited:
                continue
            
            self.visited.add(current_node)
            self.order.append(current_node)
            children = self.go(current_node)
            
            for child in children:
                
                if child not in self.visited:
                    temp_queue.append(child)
    
    
class MatrixSearcher(GraphSearcher):
    def __init__(self, df):
        super().__init__() # call constructor method of parent class
        self.df = df

    def go(self, node):
        children = []
        # TODO: use `self.df` to determine what children the node has and append them
        for node, has_edge in df.loc[node].items():
            if has_edge == 1:
                children.append(node)
        return children
    
    
class FileSearcher(GraphSearcher):
    def __init__(self):
        super().__init__()
        self.value = []
        
    def go(self, nodefile):
        file = open("file_nodes/" + str(nodefile))
        data = file.read()
        
        self.value.append(data.split('\n')[0])
        file.close
        return (data.split('\n')[1].split(","))

    def message(self):
        return ''.join(self.value)
        
        
class WebSearcher(GraphSearcher):
    def __init__(self, chrome_driver):
        super().__init__()
        self.driver = chrome_driver
        
    def go(self, node_url):
        url_list = []
        self.driver.get(node_url)
        
        li = self.driver.find_elements(by = "tag name", value = "a")
        for url in li:
            url_list.append(url.get_attribute("href"))
                            
        return url_list
        
    def table(self):
        li = []
        
        for item in self.order:
            data = pd.read_html(item)[0]
            li.append(data)
            
        return (pd.concat(li, ignore_index = True))
            
def reveal_secrets(driver, url, travellog):
        
    password = int(0)
    clue = travellog["clue"]
    for i in range(16):
        password = int((password * 10) + clue[i])
    driver.get(url)
        
    driver.find_element(value = "password").send_keys(password)
    driver.find_element(value = "attempt-button").click()
    time.sleep(2)
    
    driver.find_element(value = "securityBtn").click()  
    time.sleep(2)
    location = driver.find_element(value = "location")
    
#     driver.find_element(by = "tag name", value = "img")
    
    img_url = driver.find_element_by_id("image")
    response = requests.get(img_url.get_attribute('src'))
#     response = requests.get("https://admissions.wisc.edu/wp-content/uploads/sites/462/2020/04/aerial_UW_16mm11_6543-800x533.jpg")
#     response = requests.get(response)
    time.sleep(2)
    
    f = open("Current_Location.jpg", 'wb')
    f.write(response.content)
    f.close()

    return location.text  