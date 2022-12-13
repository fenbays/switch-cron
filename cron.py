'''
Author: hszheng hszheng2011@foxmail.com
Date: 2022-12-12 11:30:36
LastEditors: hszheng hszheng2011@foxmail.com
LastEditTime: 2022-12-13 10:12:43
FilePath: /switch-django-crontab/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from crontab import CronTab
import datetime

class Cron:
    def __init__(self, user="root"):
        self.initialize(user)

    def initialize(self, user='root'):
        """初始化"""
        self.crons = CronTab(user)

    def select(self, re_init=False):
        """查询定时任务列表"""
        if re_init:
            # 强制重新读取列表
            self.initialize()
        cron_list = []
        for job in self.crons:
            # 打印job.command
            schedule = job.schedule(date_from=datetime.datetime.now())
            cron_dict = {
                'task': (job.command).replace(r'>/dev/null 2>&1', '').split(">>")[0],
                'next': str(schedule.get_next()),
                'prev': str(schedule.get_prev()),
                "enabled": job.enabled,
                'comment': job.comment
            }
            print(cron_dict)
            cron_list.append(cron_dict)
        
        # print(cron_list)
        return cron_list

    def update(self, command, time_str, comment_name):
        """更新定时任务"""
        self.delete(comment_name)
        # 再创建任务，以达到更新的结果
        return self.add(command, time_str, comment_name)

    def disable_by_command(self, command=""):
        # cron_list = self.select()

        crons = self.crons
        for job in crons:
            if command in job.command:
                job.enable(True)
                crons.write()

    def disable_by_id(self, id):
        crons = self.crons
        crons[id].enable(False)
        crons.write()

    def enable_by_id(self, id):
        crons = self.crons
        crons[id].enable(True)
        crons.write()

if __name__ == '__main__':
    cron = Cron()
    cron.enable_by_id(0)
    # cron.disable_by_command("command 11111")
    