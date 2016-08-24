
## Decompress a string

We are given a string which is in compressed form and we have to decompress it.

```
Normal string : "AABBBCC"
Compressed form : "2A3B2C"
```
 Write a program that accepts the string in compressed form and deompress it to original form. You can assume the string will contain only positive integers and uppercase charecter alphabets. The integer precedeing the uppercase charecter specifies how many times the char appears consecutively. If a charecter has no preceding integer, assume it as 1.  
  
    
### Few testcases for better understanding the problem

- compressed = "4A2BC2A"  
    decompressed = "AAAABBCAA"

- compressed = ""  
    decompressed = ""

- compressed = "ABC"  
    decompressed = "ABC"

- compressed = "A3B5C6F"  
    decompressed = "ABBBCCCCCFFFFFF"

- compressed = "AB3C"  
    decompressed = "ABCCC"
		
- compressed = "ABCABC"  
    decompressed = "ABCABC"
		
- compressed = "A"  
    decompressed = "A"
		
- compressed = "10A"  
    decompressed = "AAAAAAAAAA"

- compressed = "10AB11C"  
    decompressed = "AAAAAAAAAABCCCCCCCCCCC"