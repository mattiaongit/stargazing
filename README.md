# Stargazing

Github's repositories stars observer.

This simple script allow to fetch stargazer information of a Github repository.

Run:
```bash
python stargazing.py --acces_token <your_access_token> --repository <repository_name>
```

This would generate a .csv (`<repository_name>-stargazers.csv`) file with all the repository stargazer information.

Output example:

| id       	| username      	| name             	| email                           	| location        	| company                     	| followers 	| following 	| public_repos 	| created_at          	| star_time           	| url                                        	|
|----------	|---------------	|------------------	|---------------------------------	|-----------------	|-----------------------------	|-----------	|-----------	|--------------	|---------------------	|---------------------	|--------------------------------------------	|
| 6830908  	| kepatopoc     	| Sergey Shmakov   	|                                 	| Moscow          	| Brand Analytics             	| 19        	| 10        	| 12           	| 2014-03-02 12:44:48 	| 2016-10-09 10:10:48 	| https://api.github.com/users/kepatopoc     	|
| 429050   	| mtwilliams    	| Michael Williams 	|                                 	| Vancouver, BC   	| @PhoenixLabsCanada          	| 67        	| 114       	| 52           	| 2010-10-06 04:16:35 	| 2016-08-17 04:36:49 	| https://api.github.com/users/mtwilliams    	|
| 36945705 	| JackELee2018  	| JackELee         	| tianxingjian1021@163.com        	| Hangzhou, China 	|                             	| 0         	| 0         	| 2            	| 2018-03-01 05:19:59 	| 2018-04-15 02:04:11 	| https://api.github.com/users/JackELee2018  	|
| 166339   	| alabarga      	| Alberto Labarga  	| alberto.labarga@scientifik.info 	| Pamplona, Spain 	| Experimental Serendipity    	| 38        	| 67        	| 465          	| 2009-12-11 20:12:55 	| 2017-11-18 14:03:16 	| https://api.github.com/users/alabarga      	|
| 608037   	| smdhruve      	| Snehal Dhruve    	|                                 	| Mumbai, India   	| Herolabs Infotech Pvt. Ltd. 	| 1         	| 5         	| 8            	| 2011-02-09 02:55:33 	| 2017-01-17 12:13:08 	| https://api.github.com/users/smdhruve      	|
| 8077469  	| andreasasprou 	| Andreas Asprou   	|                                 	| London          	|                             	| 3         	| 2         	| 20           	| 2014-07-05 21:43:08 	| 2017-09-14 19:46:53 	| https://api.github.com/users/andreasasprou 	|

## Access token
Fetch your access token from [here](https://github.com/settings/tokens)  (https://github.com/settings/tokens)


## Repository name
The repository name should be expressed in the form
profile/repostory. For example, if you wanted to fetch the stargazer of this repository (a gazillion, soon!) that would be `mattiaongit/stargazing`

## Additional configuration

Additional configuration are possible via the
- `config.json` file

Here you could setup

- Stargazer field to fetch*
- Output file name
*
By default the following fields are fetched:
```python
["id", "username", "name", "email", "location", "company", "followers", "following","public_repos", "created_at",
 "star_time", "url"]
```
