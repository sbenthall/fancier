
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def api_chunker(inputs,method,arg,n):
    """
    For API calls with a list argument of max N,
    call the method looping over chunks of inputs
    of size N
    """
    for ci in chunks(inputs,n):
        args = {}
        args[arg] = ci
        con = method(**args)

        for o in con:
            yield o
    
