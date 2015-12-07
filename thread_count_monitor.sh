#!/bin/sh

# Creates thread dump with file pattern cassandra_tdump_htc.$(date +%H%M%S.%N).txt for with thread count value >= THRD_CNT_MAX (int)
# Prereqisites:
# Set JAVA_HOME and PATH variables

CASSANDRA_PID=`cat /opt/app/logs/cassandra/cassandra.pid`
THRD_CNT_MAX=3500


threadDump() 
{
 count=10
 delay=15

 while [ $count -gt 0 ]
 do
    jstack $CASSANDRA_PID > cassandra_tdump_htc.$(date +%H%M%S.%N).txt
    sleep $delay
    let count--
    echo -n "."
 done

}

while true
do 
  PID=`cat /opt/app/logs/cassandra/cassandra.pid`
  THRD_CNT=`ps -o thcount -p $CASSANDRA_PID | grep -v THCNT`

  echo "Thread Count @ `date` --> $THRD_CNT"

  if [ $THRD_CNT -ge $THRD_CNT_MAX ]
  then
     echo "Threads maxing out - take thread dump"
     threadDump
     exit 99
  fi
  sleep 15
done