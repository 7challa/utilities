#!/bin/sh
# Script to start jstatd to connect jconsole/jvisualvm remotely
export JAVA_HOME=/opt/app/jdk1.6.0_35
export PATH=$JAVA_HOME/bin:$PATH

policy=${HOME}/visualvm.policy
[ -r ${policy} ] || cat >${policy} <<'POLICY'
grant codebase "file:${java.home}/../lib/tools.jar" {
permission java.security.AllPermission;
};
POLICY

jstatd -p 6666 -J-Djava.security.policy=${policy} &