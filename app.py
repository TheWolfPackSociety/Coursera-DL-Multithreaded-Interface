import os
from multiprocessing.pool import ThreadPool as Pool
cauth=open("login.config","r").read().replace("\n","")
def DownloadCourseraCourse(name):
    path=os.getcwd()+"\\Coursera\\"
    print(path)
    os.system('start /wait cmd /k "coursera-dl -ca '+cauth+' '+name+' --path="{}"'.format(path))
    print("course {} completed".format(name))
courses=open("list.txt","r")
course_names=[str(i).replace("\n","") for i in courses if i !=""]

pool_size=len(course_names)
pool=Pool(pool_size)
for course in course_names:
    pool.apply_async(DownloadCourseraCourse,(course,))
pool.close()
pool.join()