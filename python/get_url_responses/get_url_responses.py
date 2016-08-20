import urllib2
import threading
import time

urls = ["http://www.google.com", "http://www.facebook.com", "http://www.twitter.com",
		"http://www.quora.com", "http://www.linkedin.com", "http://www.gmail.com"]

def read_url(response_list, url, index):
	temp = urllib2.urlopen(url).read()
	response_list[index] = url

single_thread_responses = [None for i in range(len(urls))]
multi_thread_responses = [None for i in range(len(urls))]

def single_thread_get_responses(urls):
	thread_list = []
	for i in range(len(urls)):
		thread_list.append(threading.Thread(
			target=read_url, args=(single_thread_responses, urls[i], i)))

	for i in range(len(thread_list)):
		# start the thread and immediately join the thread
		# join() is a blocking call, hence it doesn't proceed
		# to next thread, thus simulating single threading
		thread_list[i].start()
		thread_list[i].join()

	return single_thread_responses

def multi_thread_get_responses(urls):
	thread_list = []
	for i in range(len(urls)):
		thread_list.append(threading.Thread(
			target=read_url, args=(multi_thread_responses, urls[i], i)))

	for i in range(len(thread_list)):
		thread_list[i].start()

	for i in range(len(thread_list)):
		thread_list[i].join()
	
	return multi_thread_responses

if __name__ == "__main__":
	start = time.time()
	responses_1 = single_thread_get_responses(urls)
	print "Time taken for processing using single thread is %s" \
			 % (time.time()-start)

	start = time.time()
	responses_2 = multi_thread_get_responses(urls)
	print "Time taken for processing using multiple threads is %s"  \
			% (time.time()-start)


