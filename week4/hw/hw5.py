def file_io(input,output):
    def file_dec(func):
        def wrapper():
            try:
                with open(input,"r",encoding="utf-8")as f:
                    deta=f.read()
            except FileNotFoundError:
                return 'not found file 404'
            
            result=func(deta)
            
            with open(output,"w",encoding="utf-8")as f:
                f.write(deta.upper())
            
            return result
        return wrapper
    return file_dec


@file_io("input.txt","test_out.txt")
def process_deta(deta):
    return str(deta.upper())


process=process_deta()
print(process)