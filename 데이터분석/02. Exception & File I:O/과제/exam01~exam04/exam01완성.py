# -*- coding: utf-8 -*-
"""
문1) 아래 코드를 실행하면 25줄에서 오류(AttributeError)가 발생되고 프로그램이 중단된다.
     원인은 패턴과 일치된 url이면 group() 메서드에 의해서 패턴과 일치된 문자열이 반환되기 
     때문에 if문이 수행 되지만 패턴과 일치되지 않은 경우에는 group() 메서드에 의해서 
     반환된 문자열이 없으므로 if문의 문장에서 오류가 발생된다. 이 코드에 예외처리를 적용하여 
     올바른 url과 잘못된 url를 구분하여 list에 저장하고 출력하시오. <출력결과> 참고      

 <출력결과> 
 올바른 url :  ['http://news.com/test', 'http://news.com/test2']
 잘못된 url :  ['now.co.kr', 'new.com', 'http//~']
"""

import re

urls = ['http://news.com/test','now.co.kr', 'new.com','http://news.com/test2', 'http//~']


proper_urls = [] # 올바른 url 저장 
wrong_urls= [] # 잘못된 url 저장 

for url in urls :
    try :
        result = re.match('^http://news', url) 
        if result.group() : # 패턴과 일치된 문자열 반환 
            proper_urls.append(url) # url 저장 
    except :
        wrong_urls.append(url) # url 저장 
        
print('올바른 url : ', proper_urls)    
print('잘못된 url : ', wrong_urls)     
'''
올바른 url :  ['http://news.com/test', 'http://news.com/test2']
잘못된 url :  ['now.co.kr', 'new.com', 'http//~']
'''



    
    
    
    
    
    
    
    