#!/bin/bash

SUCCESS_CASE=0
FAILED_CASE=0

# check case, change filename to filename---OK if success
function check_case_result() {
    result=$(awk 'END {print}' $1)
    if [ ${result} == "OK" ]; then
        let SUCCESS_CASE+=1;
        mv $1 $1"--------OK"
    else
        let FAILED_CASE+=1;
        mv $1 $1"--------FAIL"
    fi
}

# config
PROJECT_PATH="/home/william/workspace/entitlement-ci/"
VIRTWHO_PATH=${PROJECT_PATH}"testcases/virt_who/"
TESTCASE_PATH=${VIRTWHO_PATH}"all/"
home=/home/william
RESULT_PATH=${home}"/testing-result-`date +%Y%m%d`"
TESTCASE_LIST=${RESULT_PATH}"/testcase_list"
mkdir ${RESULT_PATH}

# export env
export PYTHONPATH=${PROJECT_PATH}
export HYPERVISOR_TYPE=$1
if [ "${HYPERVISOR_TYPE}" == "" ]; then
    export HYPERVISOR_TYPE=xen
fi
export RHEL_COMPOSE=RHEL-7.5
export REMOTE_IP=10.8.246.17
export SERVER_TYPE=STAGE
export VIRTWHO_SRC=default

# setup virt-who env
case ${HYPERVISOR_TYPE} in
  "xen")
    env_setup_file=${VIRTWHO_PATH}"virtwho_xen_setup.py"
    ;;
  "esx")
    env_setup_file=${VIRTWHO_PATH}"virtwho_esx_setup.py"
    ;;
  "hyperv")
    env_setup_file=${VIRTWHO_PATH}"virtwho_hyperv_setup.py"
    ;;
  "rhevm")
    env_setup_file=${VIRTWHO_PATH}"virtwho_rhevm_setup.py"
    ;;
  "vdsm")
    env_setup_file=${VIRTWHO_PATH}"virtwho_vdsm_setup.py"
    ;;
  "kvm")
    env_setup_file=${VIRTWHO_PATH}"virtwho_kvm_setup.py"
    ;;
esac
setup_res=$RESULT_PATH"/VIRT_WHO_ENV_SETUP"
touch ${setup_res}
python ${env_setup_file} &> ${setup_res}
check_case_result ${setup_res}

# run testcase
ls -l ${TESTCASE_PATH}| grep tc_ID.*.py$ | sed 's/.*tc_ID/tc_ID/g' &> ${TESTCASE_LIST}
for line in $(cat ${TESTCASE_LIST})
do
    filename=$(echo ${line} | sed 's/^tc_ID/ID/g' | sed 's/.py$//g')
    touch ${RESULT_PATH}"/"${filename}
    nosetests ${TESTCASE_PATH}"/"${line} &> ${RESULT_PATH}"/"${filename}
    check_case_result ${RESULT_PATH}"/"${filename}
done

echo "================================RUNNING RESULT================================"
echo "==============================${SUCCESS_CASE}=CASE=SUCCESSED==============================="
echo "==============================${FAILED_CASE}=CASE=FAILED=================================="
