BEFORE EVERY TEST CASE:
Start the daemon in the background (python3 ../daemon.py &)


DAEMON TEST CASES:
First navigate to the daemon_test folder (cd daemon_test)

Make everything executable (chmod -R 777 ./)

Run each test case in the format of ./daemon_tester.sh testx.py testx.out

The tester will output nothing if the test case is passed, and all expected error messages should be seen in the stdout


CALENDAR TEST CASES:
First navigate to the calendar_test folder (cd calendar_test)

Make everything executable (chmod -R 777 ./)

Run each test case in the format of ./calendar_tester.sh testx.sh testx.out

The tester will output nothing if the test case is passed (including error messages)


COMBINED TEST CASES:
First navigate to the combined_test folder (cd combined_test)

Make everything executable (chmod -R 777 ./)

Run each test case in the format of ./tester.sh testx.sh testx.out

For GET commands: the tester will output the expected events and errors in stdout for the user to compare

For ADD/DEL/UPD commands: the tester will output nothing if the test case is passed (including error messages)


INIT SCRIPT SET-UP:
Place start into the /etc.init.d folder of VM using scp

Set-up script with (rc-update add start default)

Start (rc-service start start)
Restart (rc-service start restart)
Stop (rc-service start stop)
