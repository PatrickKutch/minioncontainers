rm -f -r  Board-Instrumentation-Framework
git clone https://github.com/intel/Board-Instrumentation-Framework.git
# don't need Marvin or Minion
rm -r -f Board-Instrumentation-Framework/Minion
rm -r -f Board-Instrumentation-Framework/Marvin
rm -r -f Board-Instrumentation-Framework/*.pdf
rm Board-Instrumentation-Framework/Oscar/OscarConfig.xml


docker build -t patrickkutch/biff-oscar .
docker push patrickkutch/biff-oscar
