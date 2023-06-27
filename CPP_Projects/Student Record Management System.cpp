#include<iostream>
#include<string>
using namespace std;

string roll_no[50], name[50], address[50], DoB[50], m_num[50], course[50], p_email[50];
int total = 0;

void enter_data();
void show_data();
void search_data();
void update_data();
void delete_data();
void delete_specific();

int main()
{
	int sw;
	
	do
	{
		cout<<"EMPLOYEE RECORD MANAGEMENT SYSTEM";
		
		cout<<"\n1.Enter Record \n2.Show Record(s) \n3.Search Record \n4.Update Record \n5.Delete Record \n6.Quit \nEnter Your Option: ";
		cin>>sw;
		
		switch(sw)
		{
			case 1:
				enter_data();
				break;
			case 2:
				show_data();
				break;
			case 3:
				search_data();
				break;
			case 4:
				update_data();
				break;
			case 5:
				delete_data();
				break;
			case 6: 
				cout<<"\n\nThank you for using Employee Record Management System";
				break;
			default:
				cout<<"Entered Option was invalid. Please Enter a Valid Option";
				break;
		}
	}while(sw != 6);
}

void enter_data()
{
	int n = 0;
	
	cout<<"How Many Stuedents' Data Do You Want To Enter: ";
	cin>>n;
	
	if(total == 0)
	{
		total += n;
		
		for(int i = 0; i < n; i++)
		{
			cout<<"\nEnter Data of Student "<< i + 1<< endl<< "  ** PERSONAL DETAILS **"<< endl;
			cout<<"Enter Name: ";
			cin>>name[i];
			
			cout<<"Enter Address: ";
			cin>>address[i];
			
			cout<<"Enter Date of Birth: ";
			cin>>DoB[i];
			
			cout<<"  ** SCHOOL DETAILS **"<< endl;
			
			cout<<"Enter Roll No: ";
			cin>>roll_no[i];
			
			cout<<"Enter Course: ";
			cin>>course[i];
			
			cout<<"  ** CONTACT DETAILS **"<< endl;
			
			cout<<"Enter Parent Contact Number: ";
			cin>>m_num[i];
			
			cout<<"Enter Parent Email: ";
			cin>>p_email[i];
		}
	}
	else
	{
		for(int i = total; i < n + total; i++)
		{
			cout<<"\nEnter Data of Student "<< i + 1<< endl<< "  ** PERSONAL DETAILS **"<< endl;
			cout<<"Enter Name: ";
			cin>>name[i];
			
			cout<<"Enter Address: ";
			cin>>address[i];
			
			cout<<"Enter Date of Birth: ";
			cin>>DoB[i];
			
			cout<<"  ** SCHOOL DETAILS **\n";
			
			cout<<"Enter Roll No: ";
			cin>>roll_no[i];
			
			cout<<"Enter Course: ";
			cin>>course[i];
			
			cout<<"  ** CONTACT DETAILS **\n";
			
			cout<<"Enter Parent Contact Number: ";
			cin>>m_num[i];
			
			cout<<"Enter Parent Email: ";
			cin>>p_email[i];
		}
		total += n;
	}
	cout<<"\n\n";
}

void show_data()
{
	char op;
	
	if(total == 0)
	{
		cout<<"\n\nNo Data is Entered. \n\n";
		return;
	}
	else
	{
		cout<<"\n\nDATA OF ALL STUDENTS";
		
		for(int i = 0; i < total; i++)
		{
			cout<<"\n\nData of Student "<< i + 1;
			
			cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
			cout<<"Name: "<<name[i]<<"\n";
			cout<<"Address: "<<address[i]<<"\n";
			cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
			
			cout<<"  ** SCHOOL DETAILS **\n\n";
			cout<<"Roll No: "<<roll_no[i]<<"\n";
			cout<<"Course: "<<course[i]<<"\n\n\n";
			
			cout<<"  ** CONTACT DETAILS **\n\n";
			cout<<"Parent Mobile Number: "<<m_num[i]<<"\n";
			cout<<"Parent Email: "<<p_email[i]<<"\n\n";
			
			cout<<"Do You Wish to Continue [Y/N]: ";
			cin>>op;
			
			if(op == 'n' || op == 'N')
			{
				cout<<"\n\n\n";
				return;
			}		
		}
	}
}

void search_data()
{	
	if(total == 0)
	{
		cout<<"\n\nNo Data is Entered. \n\n";
		return;	
	}
	else
	{
		string s_id;
		bool found = false;
		
		cout<<"\n\nEnter the Roll No of the Student: ";
		cin>>s_id;
		
		for(int i = 0; i < total; i++)
		{
			if(s_id == roll_no[i])
			{
				found = true;
				cout<<"\n\nData of Student "<< i + 1;
			
				cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
				cout<<"Name: "<<name[i]<<"\n";
				cout<<"Address: "<<address[i]<<"\n";
				cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
				
				cout<<"  ** SCHOOL DETAILS **\n\n";
				cout<<"Roll No: "<<roll_no[i]<<"\n";
				cout<<"Course: "<<course[i]<<"\n\n\n";
				
				cout<<"  ** CONTACT DETAILS **\n\n";
				cout<<"Mobile Number: "<<m_num[i]<<"\n";
				cout<<"p_email roll_no: "<<p_email[i]<<"\n\n\n";
				
				cout<<"Press Enter to Return to Main Menu";
				getchar();
			}
		}
		if(found == false)
		{
			cout<<"\n\nStudent Record Not Found";
		}
	}
	cout<<"\n\n\n";
}

void update_data()
{
	if(total == 0)
	{
		cout<<"\n\nNo Data has been Entered. \n\n";
		return;
	}
	else
	{
		string u_id;
		int sw;
		
		cout<<"\n\nEnter the Roll No of the Student: ";
		cin>>u_id;
		
		for(int i = 0; i < total; i++)
		{
			if(u_id == roll_no[i])
			{
				cout<<"\n\nPrevious Data of Student "<< i + 1;
			
				cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
				cout<<"Name: "<<name[i]<<"\n";
				cout<<"Address: "<<address[i]<<"\n";
				cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
				
				cout<<"  ** SCHOOL DETAILS **\n\n";
				cout<<"Roll No: "<<roll_no[i]<<"\n";
				cout<<"Course: "<<course[i]<<"\n\n\n";
				
				cout<<"  ** CONTACT DETAILS **\n\n";
				cout<<"Mobile Number: "<<m_num[i]<<"\n";
				cout<<"p_email roll_no: "<<p_email[i]<<"\n";
				
				do
				{
					cout<<"\n\nPlease Choose what to change: \n1.Name \n2.Address \n3.Date of Birth \n4.Roll No \n5.Course \n6.Parent Mobile Number \n7.Parent Email \n8.Exit";
					cout<<"\nEnter Option: ";
					cin>>sw;
					
					switch(sw)
					{
						case 1:
							cout<<"\nEnter New Value: ";
							cin>>name[i];
							cout<<"Name Changed to "<<name[i];
							break;
						case 2:
							cout<<"\nEnter New Value: ";
							cin>>address[i];
							cout<<"Address changed to "<<address[i];
							break;
						case 3:
							cout<<"\nEnter New Value: ";
							cin>>DoB[i];
							cout<<"Date of Birth Changed to "<<DoB[i];
							break;
						case 4:
							cout<<"\nEnter New Value: ";
							cin>>roll_no[i];
							cout<<"Roll No changed to "<<roll_no[i];
							break;
						case 5:
							cout<<"\nEnter New Value: ";
							cin>>course[i];
							cout<<"Course changed to "<<course[i];
							break;
						case 6:
							cout<<"\nEnter New Value: ";
							cin>>m_num[i];
							cout<<"Parent Mobile Number Changed to "<<m_num[i];
							break;
						case 7:
							cout<<"\nEnter New Value: ";
							cin>>p_email[i];
							cout<<"Parent Email changed to "<<p_email[i];
							break;
						case 8:
							break;
						default:
							cout<<"Please Enter a Valid Option";
					}
				}while(sw != 8);
			}
		}
	}
	cout<<"\n\n\n";
}

void delete_data()
{
	if(total == 0)
	{
		cout<<"\n\nNo Data is Entered. \n\n";
		return;
	}
	else
	{
		int sw;
		
		cout<<"Please Choose What to Delete: \n1.Delete Data of Specific Student \n2.Delete Everything \n3.Exit \nEnter Option: ";
		cin>>sw;
		
		switch(sw)
		{
			case 1:
				delete_specific();
				break;
			case 2:
				total = 0;
				cout<<"\n\nSuccessfully Deleted Everything";
			case 3:
				return;
			default:
				cout<<"Please Enter a Valid Option";
		}
	}
}

void delete_specific()
{
	string d;
	bool sw = false;
	char op;
	
	cout<<"\n\nEnter the Roll No of the Student: ";
	cin>>d;
	
	for(int i = 0; i < total; i++)
	{
		if(sw == true)
		{
			name[i] = name[i + 1];
			address[i] = address[i + 1];
			DoB[i] = DoB[i + 1];
			roll_no[i] = roll_no[i + 1];
			course[i] = course[i + 1];
			m_num[i] = m_num[i + 1];
			p_email[i] = p_email[i + 1];
		}
		
		if(d == roll_no[i])
		{
			cout<<"\n\nData of Student "<< i + 1;
						
			cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
			cout<<"Name: "<<name[i]<<"\n";
			cout<<"Address: "<<address[i]<<"\n";
			cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
			
			cout<<"  ** SCHOOL DETAILS **\n\n";
			cout<<"Roll No: "<<roll_no[i]<<"\n";
			cout<<"Course: "<<course[i]<<"\n\n\n";
	
			cout<<"  ** CONTACT DETAILS **\n\n";
			cout<<"Parent Mobile Number: "<<m_num[i]<<"\n";
			cout<<"Parent Email: "<<p_email[i]<<"\n\n\n";
			
			cout<<"Do you want to Delete Data about this employee [Y/N]: ";
			cin>>op;
		}
		
		if(op == 'y' || op =='Y')
		{
			sw = true;
		}
		else if(op == 'n' || op =='N')
		{
			cout<<"\nDeletion Procedure Terminated\n";
			delete_data();
		}
	}
	if(sw == true)
	{
		total -= 1;
	}
	
	cout<<"\n\nEmployee Details Successfully Deleted\n\n\n";
}
