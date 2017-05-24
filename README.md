# LZW-Compression-Algorithm

/*  Omkar Kulkarni
	
  Algorithms and Data structions	*/ 
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Project :- LZW Compression - Implementation of the LZW Algorithm with fixed bit-length coding.
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tools :

	- Python version 2.7

Implementation :

	- Main aim is to implement LZW algorithm for compression
	- Python version 2.7 is used for implementation
	- The pogram is implemented in two parts encoding and decoding
	- Input arguments are taken in linux/windows power shell command prompt etc
	
Command prompt execution:
	- Python encododing_lzw.py input1.txt 12
	- Python decododing_lzw.py input1.lzw 12
Encoding :
	- List Data structure used to store the dictionary elements
	- input sequence is stored in string format
	- Input is taken as a .txt file from the macine e.g Input file - C:\Python27\input1.txt
	- Output is stored in a list format as 16-bit hexadecimal
	- Output file is stored in .lzw format eg encoded.lzw
	- struct library is used to pack integer in 16 bit hexadecimal format
	
Decoding:
	- .lzw file is taken as an input (encoded.lzw)
	- .lzw file is unpacked using struct library
	- List Data structure used to store the dictionary elements
	- encoded file is unpacked in a List Data structure
	- The file is decoded and original output is obtained as a string

*note

code will fail when the character given is out of the dictionary table
