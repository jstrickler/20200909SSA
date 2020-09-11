using(System.Diagnostics.Process pProcess = new System.Diagnostics.Process())
{
    pProcess.StartInfo.FileName = @"C:\Path\to\python.exe";
    pProcess.StartInfo.Arguments = "foo.py spam ham 123"; //argument
    pProcess.StartInfo.UseShellExecute = false;
    pProcess.StartInfo.RedirectStandardOutput = true;
    pProcess.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
    pProcess.StartInfo.CreateNoWindow = true; //not diplay a windows
    pProcess.Start();
    string output = pProcess.StandardOutput.ReadToEnd(); //The output result
    pProcess.WaitForExit();
}
