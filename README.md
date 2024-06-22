# Thread safe basic HTTP Connection Pool

I made this simple connection pool while going through the code base of urllib3. It is a thread safe connection pool that can only handle the requests for a single host. 

### Benchmarks

There are a few other python scripts that anyone can use to see the performance gains of using simple requests and using a connection pool with or without threading. 
