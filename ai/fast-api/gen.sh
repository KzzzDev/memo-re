#!/bin/sh
#source /anaconda/etc/profile.d/conda.sh
#conda activate ldm

#screen session
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X quit
/usr/bin/sudo -u th458-user /usr/bin/screen -dmS api
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'cd /home/th458-user/fast-api\n'
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'source /anaconda/etc/profile.d/conda.sh\n'
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'conda activate ldm\n'
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'python3 /home/th458-user/fast-api/main.py\n'
#python3 main.py
echo "finish"
