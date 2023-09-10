def domain_name(url):
    
    if "http" in url:
        return url.split('//')[1].split('.')[0] if "www" not in url else url.split('//')[1].split('.')[1]
    else:
        return url.split('.')[1] if "www" in url else url.split('.')[0]
        return 
    
    pass