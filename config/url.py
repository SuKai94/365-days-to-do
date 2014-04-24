#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                                pre_fix + 'todo.Login',
    '/365days/(\d+)',                   pre_fix + 'todo.Index',
    '/365days/(\d+)/new',               pre_fix + 'todo.New',
    '/365days/(\d+)/detail/(\d+)',      pre_fix + 'todo.Detail',
    '/365days/(\d+)/edit/(\d+)',        pre_fix + 'todo.Edit',
    '/365days/(\d+)/sendemail/(\d+)',   pre_fix + 'todo.Email',
    '/365days/(\d+)/delete/(\d+)',      pre_fix + 'todo.Delete',
    '/365days/(\d+)/finish/(\d+)',      pre_fix + 'todo.Finish',
    '/AddUser',                         pre_fix + 'todo.AddUser',
    '/Logout',                          pre_fix + 'todo.Logout',
    '/Login',                           pre_fix + 'todo.Login',
)
