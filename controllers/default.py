# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

# change background in web2py bootstrap css folder

def forum():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*3
    end = page*3
    pages = db().select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    return locals()

def createcreate123():
    form = SQLFORM(db.the_page).process(next=URL('index'))
    return locals()

def show():
    this_page = db.the_page(request.args(0,cast=int)) or redirect(URL('forum'))
    db.post.page_id.default = this_page.id
    form = SQLFORM(db.post).process()
    pagecomments = db(db.post.page_id==this_page.id).select()
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return dict(page=this_page, comments=pagecomments, form=form)

def show_all():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*25
    end = page*25
    pages = db().select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return locals()

def documents():
    page = db.the_page(request.args(0,cast=int)) or redirect(URL('forum'))
    db.documents.page_id.default = page.id
    db.documents.page_id.writable = False
    grid = SQLFORM.grid(db.documents.page_id==page.id,args=[page.id])
    return locals()

def search():
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword',_onkeyup="ajax('callack',['keyword'],'target');")),
                target_div=DIV(_id='target'))

def feed():
    return locals()

def contact():
    return locals()

def about():
    return locals()

def donations():
    return locals()

def category1():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*25
    end = page*25
    pages = db(db.the_page.category=='category1').select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return locals()

def category2():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*25
    end = page*25
    pages = db(db.the_page.category=='category2').select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return locals()

def category3():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*25
    end = page*25
    pages = db(db.the_page.category=='category3').select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return locals()

def category4():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*25
    end = page*25
    pages = db(db.the_page.category=='category4').select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return locals()

def category5():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*25
    end = page*25
    pages = db(db.the_page.category=='category5').select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return locals()

def carouselcarouselii123():
    grid = SQLFORM.grid(db.carousel, deletable=True,editable=True,user_signature=False)
    return locals()

def hypenewsthehypenewsqq123():
    grid = SQLFORM.grid(db.the_page, deletable=True,editable=True,user_signature=False)
    return locals()

def hypenewsthehypenewscc123():
    grid = SQLFORM.grid(db.post, deletable=True,editable=True,user_signature=False)
    return locals()

def callback():
    query = db.the_page.title.contains(request.vars.keyword)
    pages = db(query).select(orderby=db.the_page.title)
    links = [A(p.title,_href=URL('show',args=p.id)) for p in pages]
    return UL(*links)

def index():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*3
    end = page*3
    pages = db().select(db.the_page.ALL,
                        orderby=~db.the_page.created_on,limitby=(start,end))
    single = db(db.carousel.id==1).select()
    images = db().select(db.carousel.ALL)
    return locals()
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hype News")
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
