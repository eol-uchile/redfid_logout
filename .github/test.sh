#!/bin/dash

pip install -e /openedx/requirements/redfid_logout

cd /openedx/requirements/redfid_logout
cp /openedx/edx-platform/setup.cfg .
mkdir test_root
cd test_root/
ln -s /openedx/staticfiles .

cd /openedx/requirements/redfid_logout

DJANGO_SETTINGS_MODULE=lms.envs.test EDXAPP_TEST_MONGO_HOST=mongodb pytest redfid_logout/tests.py

rm -rf test_root
