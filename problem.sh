problem_name="$1"
mkdir $problem_name
cd $problem_name

samples_url="https://open.kattis.com/problems/$problem_name/file/statement/samples.zip"
wget --quiet $samples_url
unzip samples.zip
rm -rf samples.zip
nvim "$problem_name.py"
