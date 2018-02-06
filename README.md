# pull(what a werid repo name)

### What's this

This is a crawl script just for study

### How to run it

`python main.py`

### How it work

We have four python files in it

<table>
  <thead>
    <tr>
      <th>Python file</th>
      <th>Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>main.py</td>
      <td>start the project</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td>spider.py</td>
      <td>crawl target webside</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td>general</td>
      <td>read/write file</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td>link_finder</td>
      <td>find link in webpage</td>
    </tr>
  </tbody>
</table>

#### 总体思路：
* 创建了三个文件`queue.txt`/`crawled.txt`/`finish.txt`
* `queue.txt` 记录等待被爬的网址（文件夹的网址）
* `crawled.txt` 记录爬过的网址
* `finish.txt` 记录最终得到的文件网址

#### 一些细节实现：
* `main.py` 中建立了8个线程来进行爬取的过程
* `link_finder.py` 因为目标网站不能直接从`Request`获取html信息（反爬）， 所以在这request添加了随机`hearder` 
* `general.py`将从txt中读取的网址存为`set`类型，`set`类型在`spider.py`中用来判断url是否已经爬过`if (url in Spider.queue) or (url in Spider.crawled) or (url in Spider.finish)`表现更为高效，同时`set`类型是无序的，所以网站的爬取并不是一页一页，从上至下每个url进行获取
* `spider.py`中使用了`@staticmethod`称为静态方法，用于一些跟类有关系的功能但在运行时又不需要实例和类参与的情况

#### 其他可能的疑问：
* 什么是类 -- `class Spider` 这个Spider就是一个类
* 什么是实例 -- `spider = Spider(project_name, base_url)` 这个spider就是实例，实例是类的具化实现


#### 具体的实现

##### main.py

###### 可能的疑问:
* 什么是 `if __name__ == "__main__":` -- 这个用于表示如果我直接运行该python文件（比如 `python main.py`）那执行以下代码
* 什么是线程 -- 就是同时干很多活
* 为什么要用8条线程 -- 你可以选择更多，哈哈，多线程为了加快爬取的速度

我们直接看`if __name__ == "__main__":`这里运行了两个函数`create_workers()`和`crawl()`。
`create_workers()`中创建了8个线程，将线程绑定了`work()`函数，`work()`函数在一直等待和运行线程
`crawl()`获取`queue.txt`中等待被爬的网址，然后将其放入线程中

##### spider.py

`Spider`类的实现/爬取具体方法的实现
- `boot()` 清空/初始化三个文件夹
- `crawl_page()` 如果目标url没有被爬过，进行爬取，获取其中的url，然后将该url从等待被爬的文件`queue.txt`中删除，加入爬过`crawled.txt`的文件中。并且更新三个文件
- `add_links_to_queue_finish()` 如果获取的url是文件夹的url，则加入等待被爬`queue.txt`的序列中，否则加入最终文件夹`finish.txt`
- `update_files()`将类文件中代表着`queue` `crawled` `finish`的set变量更新到txt文件中

##### link_finder.py

###### 可能的疑问:
* bs4 是一个html解析的框架
* hearders里面的东西是我从别的地方抄来的头文件内容

`links()` 解析目标url，return里这个长长的一串可以展开写成

```
result = []
for link in soup.find_all('a', class_ = 'clearfix'):
    if 'https://' not in link.get('href'):
        result += [os.path.join(self.base_url, link.get('href'))]
return result       
                
```

通过对html的分析，我们了解到有用的url都在`<a class = 'clearfix' href = "/dir/path">`中，另外要过滤掉其中href包含https开头的url

##### general.py

###### 可能的疑问:
* 打开文件 open(file_path, 'w')
  * w 代表write
  * w+ 代表如果该文件不存在，先进行添加
  * a 代表 append
* 另外打开文件用完后记得关闭
* 另外python里面可以函数套用函数`create_data_files()`中包含`initfile()`

### TODO

 - [ ] fix HTTP Error 503: Service Temporarily Unavailable, 爬的过程太过密集，服务器拒绝