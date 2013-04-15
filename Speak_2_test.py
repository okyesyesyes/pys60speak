#import all modules
import appuifw2, sysinfo, e32, time
lt=time.ctime()

di=sysinfo.display_pixels()
#introduction screen
appuifw2.app.screen='full'
can=appuifw2.app.body=appuifw2.Canvas()

#basic app info
__name__='Speak'
__author__='Vishal Biswas'
__filename__='Speak.py'
__main__=__name__
__doc__='\t\tSpeak\n\tAn application to pronounce text as per the Text-to-Speech engine of the device\n\tReport Bugs or give suggestions or solutions for existing bugs at vshlbiswas@ymail.com\n\tUser Interaction is highly appreciated'
__version__='2.00.0'
version_info=tuple(__version__.split('.'))

def __init__(mode=''):
    appuifw2.app.title=u'Speak'
    appuifw2.app.set_tabs([],None)
    if mode=='launch':
        sys.setdefaultencoding('u8')
        globalui.global_note(u'Thank You for downloading Speak.')
        global wrap,ans,scroll,no,syst,loc,t,sav,nae,pth,ext,ppb,com,qua,dela,log
        wrap=ans=scroll=1
        no=syst=loc=sav=dela=0
        nae=u'Screenshot'
        pth=u'D:\\'
        ext=u'.jpg'
        ppb=24
        qua=100
        com='no'
        log='Off'
        try:
            #try loading settings
            dic=ini.read('C:\\system\\apps\\Speak\\settings.ini')
            appuifw2.app.screen=dic['Dsize']
            appuifw2.app.orientation=dic['Orient']
            wrap=dic['Word']
            ans=dic['Theme']
            scroll=dic['Scroll']
            sav=dic['Save']
            appuifw2.app.body=t=appuifw2.Text(skinned=ans,scrollbar=scroll,word_wrap=wrap)
            t.set_limit(dic['Limit'])
            t.color=dic['Fcolor']
            t.font=dic['Font']
            t.style=dic['Style']
            t.highlight_color=dic['Hcolor']
            envy.set_app_system(dic['System'])
            sop.set(dic['Lock'])
            pth=dic['Path']
            nae=dic['Name']
            ext=dic['Format']
            ppb=dic['Bpp']
            qua=dic['Quality']
            com=dic['Compress']
            dela=dic['Delay']
            log=dic['Log']
            if log=='On':
                if os.path.exists('c:\\private\\ebf52663'):
                    sys.stderr=open('c:\\private\\ebf52663\\ErrorLog.txt', 'a')
                elif os.path.exists('d:\\private\\ebf52663'):
                    sys.stderr=open('d:\\private\\ebf52663\\ErrorLog.txt', 'a')
                elif os.path.exists('e:\\private\\ebf52663'):
                    sys.stderr=open('e:\\private\\ebf52663\\ErrorLog.txt', 'a')
                elif os.path.exists('f:\\private\\ebf52663'):
                    sys.stderr=open('f:\\private\\ebf52663\\ErrorLog.txt', 'a')
                else:
                    sys.stderr=open('d:\\ErrorLog.txt','a')
                    globalui.global_note(u'Installation folder does not exists! Errors will be logged temporarily.', 'error')
            if sav:
                t.set(dic['Text'])
            else:
                t.set(u'Type your text here and press seak from options.')
        except:
            #else set to defaults
            envy.set_app_system(0)
            sop.set(0)
            appuifw2.app.orientation='automatic'
            appuifw2.app.screen='normal'
            appuifw2.app.body=t=appuifw2.Text(u'Type your text here and press speak from options.',skinned=ans,scrollbar=scroll,word_wrap=wrap)
    else:
        appuifw2.app.body=t
        save_set()
    appuifw2.app.menu = [(u'Speak',((u'All', speak),(u'Selected', speak_selected),(u'Word',speak_word))),
    (u'Edit',((u'Clear', t.clear), (u'Copy', copy), (u'Cut', cut),(u'Paste', paste), (u'Select all', t.select_all),(u'Select none', t.clear_selection), (u'Undo', undo),(u'Clear Undo',t.clear_undo), (u'Clear Clipboard',clr_clip))),
    (u'Find',((u'Normal',find), (u'Replace',replace))),
    (u'Text',((u'Send text as SMS', send_msg),(u'Save as txt',save),(u'Read from file', read),(u'Read from messages',read_messages))),
    (u'Goto', ((u'Go to line',gtl), (u'Start', top), (u'Middle', mid), (u'End', end), (u'Line Start', lst), (u'Line End', led), (u'Next Page', npe), (u'Previous Page', ppe))),
    (u'Text Info', info),
    (u'Settings \xbb', setting),
    (u'TTS Settings', set_speech),
    (u'Download Languages',visit)]
    appuifw2.app.exit_key_text = u'Misc'
    appuifw2.app.menu_key_text= u'Menu'
    appuifw2.app.exit_key_handler = exit_handle
    t.bind(63552, read_messages)
    t.bind(63553, save)
    t.bind(63617, setting)
    t.bind(63557, speak)
    t.bind(63586, aw)

def save_set(mod=''):
    dic={'Dsize':appuifw2.app.screen,'Orient':appuifw2.app.orientation,'Font':t.font,'Fcolor':t.color,'Style':t.style,'Hcolor':t.highlight_color,'Word':wrap,'Theme':ans,'Scroll':scroll,'Limit':no,'System':syst,'Lock':loc,'Save':sav,'Text':t.get(),'Path':pth,'Name':nae,'Format':ext,'Bpp':ppb,'Compress':com,'Quality':qua,'Delay':dela,'Log':log}
    try:
        if not os.path.exists('C:\\system\\apps\\Speak'):
            os.mkdir('C:\\system\\apps\\Speak')
        ini.write('C:\\system\\apps\\Speak\\settings.ini',dic)
        if mod!='exit':
            globalui.global_note(u'Settings save successfully','confirm')
    except:
        globalui.global_note(u'An error while saving to local file, \'settings.ini\'','error')

def gtl():
    split=t.get().split(u'\u2029')
    cul=t.get()[0:t.get_pos()].count(u'\u2029')+1
    lin=appuifw2.query(u'Go to line number(1-'+str(len(split))+')','number',cul)
    if lin!=None:
        tp=0
        if lin==0:
            lin=1
        elif lin>len(split):
            lin=len(split)
        for i in range(lin-1):
            tp+=len(split[i])+1
        t.set_pos(tp)

def screenshot():
    e32.ao_sleep(dela)
    img=graphics.screenshot()
    w=dialog.Wait(u'Saving Screenshot')
    w.show()
    try:
        num=0
        while os.path.exists(pth+nae+str(num)+ext):
            num+=1
        img.save(pth+nae+str(num)+ext,quality=qua,bpp=ppb,compression=com)
        globalui.global_note(u'Screenshot saved to '+pth+nae+str(num)+ext,'confirm')
    except:
        globalui.global_note(u'Unable to save','error')
    w.close()
    del w

def exit_handle():
    s=globalui.global_popup_menu([u'Fake Info \xbb',u'Hide',u'Visit Author\'s FB Page', u'Help \xbb', u'About', u'Exit'],u'Misc',10)
    if s==0:
        opt=globalui.global_popup_menu([u'Battery',u'Signal',u'Start Charging',u'Stop Charging'],u'Fake Info',10)
        if opt==0:
            try:
                bar=appuifw2.query(u"No. of bars(0-7)","number",7)
                indicators.set_battery(bar)
                if bar==0:
                    globalui.global_note(u'Battery empty.\nRecharge','recharge_battery')
                if bar==1:
                    globalui.global_note(u'Battery low','battery_low')
            except:
                return None
        elif opt==1:
            try:
                bar=appuifw2.query(u"No. of bars(0-7)","number",7)
                indicators.set_signal(bar)
            except:
                return None
        elif opt==2:
            globalui.global_note(u'Charging','charging')
            indicators.start_charging()
        elif opt==3:
            indicators.stop_charging()
            globalui.global_note(u'Unplug charger from power supply to save energy','text')
    elif s==1:
        try:
            appswitch.switch_to_bg(u'Speak')
        except:
            return None
    elif s==2:
        e32.start_exe('Z:\\sys\\bin\\BrowserNG.exe', (' "4 %s"' % 'http://facebook.com/vishalbiswas'))
    elif s==3:
        an = globalui.global_popup_menu([u'General', u'Shortcuts', u'Menu',u'Known Bugs',u'Fake Info'], u'Select Help Conent:')
        if an==0:
            msgquery.infopopup(u"Type any text in the textarea and press speak from options to make me say your phrase. You can use any languages which your phone supports. You can download more languages for Text To Speech from Nokia's Official Website.",u'General',msgquery.OKREmpty)
        if an==1:
            msgquery.infopopup(u'Middle Selection Key: Speak!\nDial Key: Combine Shortcurts\nRight Soft Key: Miscellaneous tools\nCamera Key: Settings\nVolume Up: Read Text from messages\nVolume Down: Save as txt\nCombination Shortcuts:-\nDial: Screenshot\nClear: Clear all\nUp: Page up\nDown: Page down\nLeft: Start of line\nRight: End of line\nVolume Up:Start of Document\nVolume Down: End of Document\nMiddle Selection: Send text as SMS\n1: Cut\n2: Undo\n3: Text Info\n4: Speak Word\n5: Speak selected\n6: TTS Settings\n7: Reset settings\n8: Find text\n9: Replace text\n0: Exit\n*: Download Languages\n#: Go to line\nCamera: Open file',u'Shortcuts',msgquery.OKREmpty)
        if an==2:
            msgquery.infopopup(u'Speak: Speak the text\nEdit: Text related functions like copy, paste, undo, etc\nText: Operations involving the text in the textarea\nGoto: Go to the specific section of the page or navigate through the text\nText Info: Information of the text\nSettings: All the apps\' preferences\nDownload Languages: Download text-to-speech languages from Nokia\'s Official Site',u'Menu',msgquery.OKREmpty)
        if an==3:
            msgquery.infopopup(u'1. Applications closes unexpectedly when selecting path of saving or reading files\n2. Changing highlight style resets the font style\n3. The set values in settings are not shown instantly in the settings listbox\n4. Some fonts\' anti-aliasing settings cannot be changed',u'Known Bugs',msgquery.OKREmpty)
        if an==4:
            msgquery.infopopup(u'All the changes made by this function are purely fake. They are used to just fool others. I have made it as real as possible.\nBattery: Change the number of bars shown in the battery pane\nSignal: Change the number of bars shown in the signal pane\nStart Charging: Simulates battery charging but in reality doesn\'t charges battery\nStop Charging: Stops the simulation of battery as if battery is full',u'Fake Info',msgquery.OKREmpty)
    elif s==4:
        txt=u'Version: '+__version__+'\nMain App: Ensymble\nModded by: vishalbiswas\nE-mail: vshlbiswas@ymail.com\nUID: '+appuifw2.app.uid().upper()+u'\nPath: '+appuifw2.app.full_name().upper()+u'\nS/W Version: '+sysinfo.sw_version()+u'\nPython Version: '+e32.pys60_version+'\nDetailed Python Version: '+sys.version
        caps='\nCapabilities Granted: '
        if e32.pys60_version_info[0]>=2:
            for i in e32.get_capabilities():
                if i==e32.get_capabilities()[0]:
                    caps+=i
                else:
                    caps+='+'+i
        else:
            caps+=envy.app_capabilities()
        msgquery.infopopup(txt+caps,u'Speak',msgquery.OKREmpty)
    elif s==5:
        quit_ask()

def visit():
    e32.start_exe('Z:\\sys\\bin\\BrowserNG.exe', (' "4 %s"' % 'http://www.nokia.com/global/support/text-to-speech-s60-downloads/'))

def clr_clip():
    try:
        open('D:\\system\\Data\\Clpboard.cbd','w')
        globalui.global_note(u'Clipboard Cleared','confirm')
    except:
        return None

def top():
    t.set_pos(0)

def mid():
    length = t.len()
    if (length%2)==1:
        posit=((length+1)/2)
    else:
        posit=(length/2)
    t.set_pos(posit)

def lst():
    t.move(appuifw2.EFLineBeg)

def led():
    t.move(appuifw2.EFLineEnd)

def npe():
    t.move(appuifw2.EFPageDown)

def ppe():
    t.move(appuifw2.EFPageUp)

def info():
    split=t.get().split(u'\u2029')
    cul=t.get()[0:t.get_pos()].count(u'\u2029')+1
    try:
        global e
        enc=e
    except:
        enc=sys.getdefaultencoding()
    msgquery.infopopup(u'Characters: '+str(t.len())+u'\nPosition: '+str(t.get_pos())+u'\nLaunch Time: '+lt+u'\nEncoding: '+enc+u'\nLine Number: '+str(cul)+u'('+str(len(split))+u')\nFont: '+t.font[0]+u'\nFont Height: '+str(t.font[1]),u'Text Information',msgquery.OKREmpty)

def end():
    t.set_pos(t.len())

def speak():
    textToSpeak = appuifw2.app.body.get()
    if textToSpeak == '' or textToSpeak.isspace():
        globalui.global_note(u'Type something to speak!', 'error')
    else:
        w=dialog.Wait(u'Speaking...')
        w.show()
        au = audio.say(textToSpeak)
        w.close()
        del w

def quit_ask():
    opt=globalui.global_query(u'Do you want to exit?',10)
    if opt==1:
        save_set('exit')
        app_lock.signal()
        appuifw2.app.set_exit()

def send_msg():
    txt = appuifw2.app.body.get()
    opt=globalui.global_popup_menu([u'From Contacts',u'Enter Manually'],u'Choose Number')
    if opt==1:
        num = appuifw2.query(u'Type the Number', 'float')
        try:
            num=int(num)
        except:
            return None
    elif opt==0:
        nam=appuifw2.query(u'Type the Name','text')
        con=contacts.ContactsDb()
        ls=con.find(nam)
        lst=[]
        try:
            for i in ls:
               lst.append(i.title)
            lst.sort()
            se=appuifw2.selection_list(lst,True)
            num=ls[se][0].value
        except:
            return None
    try:
        if num==None:
            return None
        else:
            pro = sysinfo.active_profile()
            if pro == 'offline' : 
                globalui.global_note(u'Phone in Offline profile! Message will be sent later.', 'warn')
            else:
                net = sysinfo.signal_bars()
                if net == 0 : 
                    globalui.global_note(u'No signal! Message will be sent later.', 'warn')
                pass
            m=messaging.sms_send(num, txt)
            globalui.global_note(u'Message Submitted succesfully', 'confirm')
    except:
        return None

def set_speech():
    try:
        e32.start_exe('z:\\sys\\bin\\ttsmanager.exe', '')
    except:
        appuifw2.note(u'Unable to Open', 'error')

def paste():
    if t.can_paste() : 
        t.paste()
    else : 
        globalui.global_note(u'Unable to paste!', 'error')

def copy():
    if t.can_copy():
        t.copy()
        globalui.global_note(u'Copied!', 'confirm')
    else:
        globalui.global_note(u'Nothing selected for copying!', 'error')

def cut():
    if t.can_cut():
        t.cut()
        globalui.global_note(u'Cutting Complete!', 'confirm')
    else:
        globalui.global_note(u'Nothing selected for cutting!', 'error')

def undo():
    if t.can_undo() : 
        t.undo()
    else : 
        globalui.global_note(u'Nothing to undo!', 'error')

def read():
    encods=['u8','u16','ascii','cp1251','iso8859','base64','hex']
    pat=filebrowser.select('Open file')
    if pat!=None:
        global e
        for e in encods:
            try:
                fil=open(pat,"r")
                w=dialog.Wait(u'Decoding file using %s...'%e)
                w.show()
                e32.ao_sleep(1)
                if pat.endswith(u'.doc'):
                    try:
                        tet=fil.read()
                        t.set(tet[tet.find('\x02\x00\x0c\x01'+'\x00'*74)+78:tet.find('\x0d'+'\x00'*191)].decode(e))
                        globalui.global_note(u'File loaded','confirm')
                        break
                    except:
                        if e!=encods[len(encods)-1]:
                            continue
                        else:
                            globalui.global_note(u'Unable to decode file','error')
                else:
                    try:
                        t.set(fil.read().decode(e))
                        globalui.global_note(u'File loaded','confirm')
                        break
                    except:
                        if e!=encods[len(encods)-1]:
                            continue
                        else:
                            globalui.global_note(u'Unable to decode file','error')
                w.hide()
            except:
                globalui.global_note(u'Unable to open file','error')
            e32.ao_yield()
    else:
        return None

def save():
    temp=t.get()
    fol=filebrowser.select('Save as txt',True)
    if fol!=None:
        try:
            name=appuifw2.query(u"File Name(.txt)","text",u"Document")
            nam=fol+name+".txt"
        except:
            return None
        try:
            if os.path.exists(nam):
                req=globalui.global_query(name+u" already exists. Do you want to overwrite?")
                if req==1:
                    fil=file(nam,"w")
                    fil.write(temp.encode('u16').replace('\x29\x20','\x0d\x00\x0a\x00'))
                    globalui.global_note(u"Saved to "+nam,'confirm')
            else:
                fil=file(nam,"w")
                fil.write(temp.encode('u16').replace('\x29\x20','\x0d\x00\x0a\x00'))
                globalui.global_note(u"Saved to "+nam,'confirm')
        except:
            globalui.global_note(u"Unable to save","error")

def speak_selected():
    if t.get_selection()[2]=='' or t.get_selection()[2].isspace():
        globalui.global_note(u'Nothing selected','warn')
    else:
        w=dialog.Wait(u'Speaking...')
        w.show()
        audio.say(t.get_selection()[2])
        w.close()
        del w

def read_messages():
    try:
        opt=globalui.global_popup_menu([u'Inbox \xbb',u'Outbox \xbb',u'Sent \xbb',u'Draft \xbb'],u'Choose Folder')
        if opt==0:
            fold=inbox.EInbox
        if opt==1:
            fold=inbox.EOutbox
        if opt==2:
            fold=inbox.ESent
        if opt==3:
            fold=inbox.EDraft
        fol=inbox.Inbox(fold)
        meid=fol.sms_messages()
        if meid!=[]:
            global som, old
            old=[appuifw2.app.menu_key_text,appuifw2.app.menu,appuifw2.app.exit_key_text,appuifw2.app.exit_key_handler,appuifw2.app.title]
            som=[]
            m=[]
            for i in meid:
                som.append((fol.content(i),fol.address(i),fol.time(i)))
                m.append((fol.content(i),fol.address(i)))
            appuifw2.app.body=appuifw2.Listbox(m,mes)
            appuifw2.app.title=u'Select Message'
            appuifw2.app.menu=[(u'Info',minf),(u'Close',stop)]
            appuifw2.app.exit_key_handler=stop
            appuifw2.app.menu_key_text=u'Messages'
            appuifw2.app.exit_key_text=u'Close'
            ao=e32.Ao_lock()
            ao.wait()
        else:
            appuifw2.note(u'Folder Empty','error')
            read_messages()
    except:
        return None

def mes():
    id=appuifw2.app.body.current()
    t.set(som[id][0])
    stop()

def minf():
    id=appuifw2.app.body.current()
    txt=u'Phone: %s\nTime: %s\nMessage: %s'%(som[id][1],som[id][2],som[id][0])
    msgquery.infopopup(txt,som[id][0],msgquery.OKREmpty)

def reset():
    try:
        opt=globalui.global_query(u'All settings will be reverted back to default. Continue?')
        if opt==1:
            open('c:\\system\\apps\\speak\\settings.ini','w')
            globalui.global_note(u'Settings resetted!','confirm')
            __init__('launch')
    except:
        return None

def setting():
    appuifw2.app.menu=[(u'Reset all Settings',reset),(u'Save & Close',__init__),(u'Exit',quit_ask)]
    appuifw2.app.exit_key_handler=__init__
    appuifw2.app.exit_key_text=u'Save'
    appuifw2.app.set_tabs([u'App',u'Format',u'Text',u'Screenshot'],selecte)
    selecte()

def find():
    global txt, srh, old
    try:
        txt=appuifw2.query(u'Enter search content(case sensitive)','text',txt)
    except:
        txt=appuifw2.query(u'Enter search content(case sensitive)','text')
    if txt!=None:
        srh=globalui.global_popup_menu([u'Forward',u'Backward'],u'Search Direction')
    if txt!=None and srh!=None:
        if srh==0:
            sp=t.get().find(txt)
            if sp!=-1:
                t.set_selection(sp,sp+len(txt))
                old=[appuifw2.app.menu_key_text,appuifw2.app.menu]
                appuifw2.app.menu_key_text=u'Search'
                appuifw2.app.menu=[(u'Next',next),(u'Previous',prev),(u'Stop',stop)]
            else:
                globalui.global_note(u'Text not found','warn')
        elif srh==1:
            sp=t.get().rfind(txt)
            if sp!=-1:
                t.set_selection(sp,sp+len(txt))
                old=[appuifw2.app.menu_key_text,appuifw2.app.menu]
                appuifw2.app.menu_key_text=u'Search'
                appuifw2.app.menu=[(u'Next',next),(u'Previous',prev),(u'Stop',stop)]
            else:
                globalui.global_note(u'Text not found','warn')
        else:
            return None

def next():
    if srh==0:
        nsp=t.get().find(txt,t.get_pos())
        if nsp!=-1:
            t.set_selection(nsp,nsp+len(txt))
        else:
            globalui.global_note(u'Text Not found','warn')
    elif srh==1:
        nsp=t.get().rfind(txt,0,t.get_pos())
        if nsp!=-1:
            t.set_selection(nsp,nsp+len(txt))
        else:
            globalui.global_note(u'Text Not found','warn')

def prev():
    if srh==0:
        psp=t.get().rfind(txt,0,t.get_pos())
        if psp!=-1:
            t.set_selection(psp,psp+len(txt))
        else:
            globalui.global_note(u'Text not found','warn')
    elif srh==1:
        psp=t.get().find(txt,t.get_pos())
        if psp!=-1:
            t.set_selection(psp,psp+len(txt))
        else:
            globalui.global_note(u'Text not found','warn')

def stop():
    appuifw2.app.menu_key_text=old[0]
    appuifw2.app.menu=old[1]
    try:
        appuifw2.app.exit_key_text=old[2]
        appuifw2.app.exit_key_handler=old[3]
        appuifw2.app.title=old[4]
        appuifw2.app.body=t
    except:
        return None

def replace():
    global otext, rtext
    try:
        otext=appuifw2.query(u'Type the old text(case sensitive)','text',otext)
    except:
        otext=appuifw2.query(u'Type the old text(case sensitive)','text')
    if otext!=None:
        try:
            rtext=appuifw2.query(u'Type the replace text(case sensitive)','text',rtext)
        except:
            rtext=appuifw2.query(u'Type the replace text(case sensitive)','text')
    if otext!=None and rtext!=None:
        try:
            nor=appuifw2.query(u'Type no. of replaces(optional)','number',nor)
        except:
            nor=appuifw2.query(u'Type no. of replaces(optional)','number')
        if nor!=None and nor!=0:
            t.set(t.get().replace(otext,rtext,nor))
        else:
            t.set(t.get().replace(otext,rtext))

def selecte(sele=0,mode=''):
    global l
    if sele==0:
        if syst:
            systt=u'On'
        else:
            systt=u'Off'
        if loc:
            lockt=u'On'
        else:
            lockt=u'Off'
        appuifw2.app.title=u'Application'
        lsb=[(u'Display Size \xbb',appuifw2.app.screen.decode('u8')),(u'Screen Orientation \xbb',appuifw2.app.orientation.decode('u8')),(u'System App',systt),(u'Application Lock',lockt),(u'Local Error Log',log)]
        appuifw2.app.body=l=appuifw2.Listbox(lsb,ap)
    elif sele==1:
        if t.font[2]>=16 and t.font[2]<32:
            antit=u'On'
        elif t.font[2]>31 or t.font[2]==None:
            antit=u'Off'
        appuifw2.app.title=u'Formatting'
        lsb=[(u'Font \xbb',t.font[0]),(u'Font Color \xbb',str(t.color).decode('u8')),(u'Font Size',str(t.font[1]).decode('u8')),(u'Anti Aliasing',antit),(u'Font Style \xbb',u'Font formatting styles'),(u'Highlight Color',str(t.highlight_color).decode('u8')),(u'Highlight Style \xbb',u'Highlight styles namely rounded, shadow, standard')]
        appuifw2.app.body=l=appuifw2.Listbox(lsb,fh)
    elif sele==2:
        if wrap:
            wrapt=u'On'
        else:
            wrapt=u'Off'
        if ans:
            skint=u'On'
        else:
            skint=u'Off'
        if scroll:
            scrollt=u'On'
        else:
            scrollt=u'Off'
        if no==0 or no==None:
            limitt=u'Off'
        else:
            limitt=str(no)
        if sav:
            savt=u'On'
        else:
            savt=u'Off'
        appuifw2.app.title=u'Text'
        lsb=[(u'Word Wrap',wrapt),(u'Theme Background',skint),(u'Scroll Bar',scrollt),(u'Character Limit',limitt),(u'Store text on Exit',savt)]
        appuifw2.app.body=l=appuifw2.Listbox(lsb,tex)
    elif sele==3:
        appuifw2.app.title=u'Screenshot'
        lsb=[(u'Path for saving',pth),(u'Base File Name',nae),(u'Extension',ext),(u'Bits Per Pixel',ppb),(u'Quality',qua),(u'Image Compression',com),(u'Capture Delay',str(dela)+u' seconds')]
        appuifw2.app.body=l=appuifw2.Listbox(lsb,scrs)
    if mode=='r':
        l.set_list(lsb,cur)
    l.bind(63586, screenshot)

def scrs():
    global pth,nae,ext,ppb,qua,com,dela,cur
    cur=l.current()
    if cur==0:
        temp=pth
        pth=filebrowser.select('Save Screenshots',True)
        if pth==None:
            pth=temp
        else:
            pth=pth.decode('u8')
    elif cur==1:
        temp=nae
        nae=appuifw2.query(u'Base File Name','text',nae)
        if nae==None:
            nae=temp
    elif cur==2:
        op=globalui.global_popup_menu([u'JPEG',u'PNG'],u'Extension')
        if op==0:
            ext=u'.jpg'
        elif op==1:
            ext=u'.png'
    elif cur==3:
        opt=globalui.global_popup_menu([u'1',u'8',u'24'],u'BPP')
        if opt==0:
            ppb=1
        elif opt==1:
            ppb=8
        elif opt==2:
            ppb=24
    elif cur==4:
        an=appuifw2.query(u'Quality (%)','number',qua)
        if an!=None:
            if an>100:
                qua=100
            else:
                qua=an
    elif cur==5:
        opti=globalui.global_popup_menu([u'No Compression',u'Default',u'Fast',u'Best'],u'Image Compression')
        if opti!=None:
            if opti==0:
                com='no'
            elif opti==1:
                com='default'
            elif opti==2:
                com='fast'
            elif opti==3:
                com='best'
    elif cur==6:
        sec=appuifw2.query(u'Capture Delay(seconds)','float',dela)
        if sec!=None:
            if sec<0:
                sec=-sec
            dela=sec
    selecte(3,'r')

def tex():
    global cur
    cur=l.current()
    if cur==0:
        global wrap
        wrap=not wrap
    elif cur==1:
        global ans
        ans=not ans
    elif cur==2:
        global scroll
        scroll=not scroll
    elif cur==3:
        global no
        temp=no
        no=appuifw2.query(u'No. of Characters(0:No Limit)','number',no)
        if no==None:
            no=temp
        try:
            t.set_limit(no)
        except:
            return None
        del temp
    elif cur==4:
        global sav
        sav=not sav
    selecte(2,'r')

def fh():
    global cur
    cur=l.current()
    if cur==0:
        flist=appuifw2.available_fonts()
        flist.insert(0,u'Associated Fonts \xbb')
        fcho=globalui.global_popup_menu(flist,u"Select Font",10)
        si=t.font[1]
        fl=t.font[2]
        if fcho==-1:
            return None
        elif fcho==0:
            opt=globalui.global_popup_menu([u'Normal',u'Annotation',u'Title',u'Legend',u'Symbol',u'Dense'],u'Associated Fonts')
            if opt==0:
                t.font='normal'
            elif opt==1:
                t.font='annotation'
            elif opt==2:
                t.font='title'
            elif opt==3:
                t.font='legend'
            elif opt==4:
                t.font='symbol'
            elif opt==5:
                t.font='dense'
        else:
            t.font=(flist[fcho],si,fl)
        t.apply()
    elif cur==1:
        coln=globalui.global_popup_menu([u'Black',u'Bright yellow',u'Dark green',u'Bright red',u'Bright blue',u'Medium gray',u'Blue',u'Pink',u'Orange',u'Violet',u'Type Manually'],u'Select Font Color')
        if coln==0:
            t.color=0
        elif coln==1:
            t.color=0xffff00
        elif coln==2:
            t.color=0x004000
        elif coln==3:
            t.color=0xff0000
        elif coln==4:
            t.color=255
        elif coln==5:
            t.color=(128,128,128)
        elif coln==6:
            t.color=(0,255/2,255*0.9)
        elif coln==7:
            t.color=0xef80c0
        elif coln==8:
            t.color=(255,255/2,0)
        elif coln==9:
            t.color=(128,128,192)
        elif coln==10:
            f=appuifw2.Form([(u'Red Color Value','number',t.color[0]),(u'Green Color Value','number',t.color[1]),(u'Blue Color Value','number',t.color[2])],appuifw2.FFormEditModeOnly | appuifw2.FFormDoubleSpaced)
            f.execute()
            try:
                t.color=(f[0][2],f[1][2],f[2][2])
            except:
                return None
        t.apply()
    elif cur==2:
        si=appuifw2.query(u'Type the font size(in pixels)','number',t.font[1])
        if si!=-1 and si!=None:
            f=t.font[0]
            fl=t.font[2]
            t.font=(f,si,fl)
            t.apply()
    elif cur==3:
        if t.font[2]<=16 and t.font[2]<32:
            t.font=(t.font[0],t.font[1],32)
        elif t.font[2]>31 or t.font[2]==None:
            t.font=(t.font[0],t.font[1],16)
        t.apply()
    elif cur==4:
        i=appuifw2.multi_selection_list([u'Bold',u'Underline',u'Italic',u'Strikethrough'],'checkbox')
        if i!=():
            t.style=0
            for c in i:
                if c==0:
                    if t.style=='':
                        t.style=appuifw2.STYLE_BOLD
                    else:
                        t.style=t.style | appuifw2.STYLE_BOLD
                elif c==1:
                    if t.style=='':
                        t.style=appuifw2.STYLE_UNDERLINE
                    else:
                        t.style=t.style | appuifw2.STYLE_UNDERLINE
                elif c==2:
                    if t.style=='':
                        t.style=appuifw2.STYLE_ITALIC
                    else:
                        t.style=t.style | appuifw2.STYLE_ITALIC
                elif c==3:
                    if t.style=='':
                        t.style=appuifw2.STYLE_STRIKETHROUGH
                    else:
                        t.style=t.style | appuifw2.STYLE_STRIKETHROUGH
        t.apply()
    elif cur==5:
        f=appuifw2.Form([(u'Red Color Value','number',t.highlight_color[0]),(u'Green Color Value','number',t.highlight_color[1]),(u'Blue Color Value','number',t.highlight_color[2])],appuifw2.FFormEditModeOnly | appuifw2.FFormDoubleSpaced)
        f.execute()
        try:
            t.highlight_color=(f[0][2],f[1][2],f[2][2])
        except:
            return None
        t.apply()
    elif cur==6:
        s=globalui.global_popup_menu([u'Standard',u'Rounded',u'Shadow'],u'Highlight Style')
        if s==0:
            t.style=t.style | appuifw2.HIGHLIGHT_STANDARD
        elif s==1:
           t.style=t.style | appuifw2.HIGHLIGHT_ROUNDED
        elif s==2:
            t.style=t.style | appuifw2.HIGHLIGHT_SHADOW
        t.apply()
    selecte(1,'r')

def aw():
    appuifw2.app.navi_text=u'Shortcut'.center(30)
    t.read_only=1
    t.focus=0
    t.bind(63586, screenshot)
    t.bind(63552, top)
    t.bind(63553, end)
    t.bind(63617, read)
    t.bind(63557, send_msg)
    t.bind(63498, npe)
    t.bind(63497, ppe)
    t.bind(8, t.clear)
    t.bind(35, gtl)
    t.bind(42, visit)
    t.bind(48, quit_ask)
    t.bind(49, cut)
    t.bind(50, undo)
    t.bind(51, info)
    t.bind(52, speak_word)
    t.bind(53, speak_selected)
    t.bind(54, set_speech)
    t.bind(55, reset)
    t.bind(56, find)
    t.bind(57, replace)
    e32.ao_sleep(1)
    appuifw2.app.navi_text=None
    t.read_only=0
    t.focus=1
    t.bind(63586, aw)
    t.bind(63552, read_messages)
    t.bind(63553, save)
    t.bind(63617, setting)
    t.bind(63557, speak)
    t.bind(63498, None)
    t.bind(63497, None)
    t.bind(8, None)
    t.bind(35, None)
    t.bind(42, None)
    t.bind(48, None)
    t.bind(49, None)
    t.bind(50, None)
    t.bind(51, None)
    t.bind(52, None)
    t.bind(53, None)
    t.bind(54, None)
    t.bind(55, None)
    t.bind(56, None)
    t.bind(57, None)

def ap():
    global cur
    cur=l.current()
    if cur==0:
        s = globalui.global_popup_menu([u'Normal', u'Full', u'Hide Title Bar'], u'Display Size')
        if s==0:
            appuifw2.app.screen='normal'
        if s==1:
            appuifw2.app.screen='full'
        if s==2:
            appuifw2.app.screen='large'
    elif cur==1:
        opt=globalui.global_popup_menu([u'Automatic',u'Portrait',u'Landscape'],u'Screen Orientation')
        if opt==0:
            appuifw2.app.orientation='automatic'
        elif opt==2:
            appuifw2.app.orientation = 'landscape'
        elif opt==1:
            appuifw2.app.orientation = 'portrait'
    elif cur==2:
        global syst
        syst=not syst
        envy.set_app_system(syst)
    elif cur==3:
        global loc
        loc=not loc
        sop.set(loc)
    elif cur==4:
        global log
        if log=='Off':
            log='On'
        else:
            log='Off'
    selecte(0,'r')

def new_msg(id):
    if globalui.global_query(u'New message received. Do you want to speak it?',10):
        w=dialog.Wait(u'Speaking...')
        w.show()
        audio.say(box.content(id))
        w.close()
        del w
    else:
        return None

def speak_word():
    w=dialog.Wait(u'Speaking...')
    w.show()
    audio.say(t.get(t.get_word_info(t.get_pos())[0],t.get_word_info(t.get_pos())[1]))
    w.close()
    del w

if sysinfo.battery()<=10:
    if globalui.global_query(u'Battery is low\nSpeak drains battery fast, Continue?')==0:
        os.abort()
pro=sysinfo.active_profile()
if pro=='offline' or pro=='silent':
    if globalui.global_query(u'Phone in '+pro+' profile, Continue?')==0:
        os.abort()

def load(percent=6.25):
    can.clear((255,255,255))
    can.rectangle([(0),(0),(di[0]*percent/100),(di[1])],outline=(200,200,200),fill=(100,100,100),width=3)
    can.text((di[0]/2-15,di[1]/2+10),str(int(percent)).decode('u8')+u'%',(13,49,102),'title')
    e32.ao_sleep(0.0000000001)

load(6.25)
import audio
load(12.5)
import os
load(18.75)
import globalui
load(25)
import sys
load(31.25)
import indicators
load(37.5)
import ini
load(43.75)
import envy
load(50)
import appswitch
load(56.25)
import sop
load(62.5)
import msgquery
load(68.75)
import dialog
load(75)
import messaging
load(81.25)
import inbox
load(87.5)
import contacts
load(93.75)
import filebrowser
load(100)
import graphics
__init__('launch')
box=inbox.Inbox()
box.bind(new_msg)
app_lock = e32.Ao_lock()
app_lock.wait()
