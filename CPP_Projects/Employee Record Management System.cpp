#include<iostream>
#include<string>
using namespace std;

string id[50], name[50], address[50], DoB[50], m_num[50], DoJ[50], email[50];
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
		
		cout<<"\n1.Enter Data \n2.Show Data \n3.Search \n4.Update \n5.Delete \n6.Quit \nEnter Your Option: ";
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
	
	cout<<"How Many Employees' Data Do You Want To Enter: ";
	cin>>n;
	
	if(total == 0)
	{
		total += n;
		
		for(int i = 0; i < n; i++)
		{
			cout<<"\nEnter Data of Employee "<< i + 1<< endl<< "  ** PERSONAL DETAILS **"<< endl;
			cout<<"Enter Name: ";
			cin>>name[i];
			
			cout<<"Enter Address: ";
			cin>>address[i];
			
			cout<<"Enter Date of Birth: ";
			cin>>DoB[i];
			
			cout<<"  ** WORK DETAILS **"<< endl;
			
			cout<<"Enter ID: ";
			cin>>id[i];
			
			cout<<"Enter Date of Joining: ";
			cin>>DoJ[i];
			
			cout<<"  ** CONTACT DETAILS **"<< endl;
			
			cout<<"Enter Contact Number: ";
			cin>>m_num[i];
			
			cout<<"Enter Email Id: ";
			cin>>email[i];
		}
	}
	else
	{
		for(int i = total; i < n + total; i++)
		{
			cout<<"\nEnter Data of Employee "<< i + 1<< endl<< "  ** PERSONAL DETAILS **"<< endl;
			cout<<"Enter Name: ";
			cin>>name[i];
			
			cout<<"Enter Address: ";
			cin>>address[i];
			
			cout<<"Enter Date of Birth: ";
			cin>>DoB[i];
			
			cout<<"  ** WORK DETAILS **\n";
			
			cout<<"Enter ID: ";
			cin>>id[i];
			
			cout<<"Enter Date of Joining: ";
			cin>>DoJ[i];
			
			cout<<"  ** CONTACT DETAILS **\n";
			
			cout<<"Enter Contact Number: ";
			cin>>m_num[i];
			
			cout<<"Enter Email Id: ";
			cin>>email[i];
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
		cout<<"\n\nDATA OF ALL EMPLOYEES";
		
		for(int i = 0; i < total; i++)
		{
			cout<<"\n\nData of employee "<< i + 1;
			
			cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
			cout<<"Name: "<<name[i]<<"\n";
			cout<<"Address: "<<address[i]<<"\n";
			cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
			
			cout<<"  ** WORK DETAILS **\n\n";
			cout<<"ID: "<<id[i]<<"\n";
			cout<<"Date of Joining: "<<DoJ[i]<<"\n\n\n";
			
			cout<<"  ** CONTACT DETAILS **\n\n";
			cout<<"Mobile Number: "<<m_num[i]<<"\n";
			cout<<"Email ID: "<<email[i]<<"\n\n";
			
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
		
		cout<<"\n\nEnter the ID of the Employee: ";
		cin>>s_id;
		
		for(int i = 0; i < total; i++)
		{
			if(s_id == id[i])
			{
				found = true;
				cout<<"\n\nData of Employee "<< i + 1;
			
				cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
				cout<<"Name: "<<name[i]<<"\n";
				cout<<"Address: "<<address[i]<<"\n";
				cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
				
				cout<<"  ** WORK DETAILS **\n\n";
				cout<<"ID: "<<id[i]<<"\n";
				cout<<"Date of Joining: "<<DoJ[i]<<"\n\n\n";
				
				cout<<"  ** CONTACT DETAILS **\n\n";
				cout<<"Mobile Number: "<<m_num[i]<<"\n";
				cout<<"Email ID: "<<email[i]<<"\n\n\n";
				
				cout<<"Press Enter to Return to Main Menu";
				getchar();
			}
		}
		if(found == false)
		{
			cout<<"\n\nEmployee Data Not Found";
		}
	}
	cout<<"\n\n\n";
}

void update_data()
{
	if(total == 0)
	{
		cout<<"\n\nNo Data is Entered. \n\n";
		return;
	}
	else
	{
		string u_id;
		int sw;
		
		cout<<"\n\nEnter the ID of the Employee: ";
		cin>>u_id;
		
		for(int i = 0; i < total; i++)
		{
			if(u_id == id[i])
			{
				cout<<"\n\nPrevious Data of Employee "<< i + 1;
			
				cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
				cout<<"Name: "<<name[i]<<"\n";
				cout<<"Address: "<<address[i]<<"\n";
				cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
				
				cout<<"  ** WORK DETAILS **\n\n";
				cout<<"ID: "<<id[i]<<"\n";
				cout<<"Date of Joining: "<<DoJ[i]<<"\n\n\n";
				
				cout<<"  ** CONTACT DETAILS **\n\n";
				cout<<"Mobile Number: "<<m_num[i]<<"\n";
				cout<<"Email ID: "<<email[i]<<"\n";
				
				do
				{
					cout<<"\n\nPlease Choose what to change: \n1.Name \n2.Address \n3.Date of Birth \n4.ID \n5.Date of Joining \n6.Mobile Number \n7.Email ID \n8.Exit";
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
							cin>>id[i];
							cout<<"ID changed to "<<id[i];
							break;
						case 5:
							cout<<"\nEnter New Value: ";
							cin>>DoJ[i];
							cout<<"Date of Joinging changed to "<<DoJ[i];
							break;
						case 6:
							cout<<"\nEnter New Value: ";
							cin>>m_num[i];
							cout<<"Mobile Number Changed to "<<m_num[i];
							break;
						case 7:
							cout<<"\nEnter New Value: ";
							cin>>email[i];
							cout<<"Email ID changed to "<<email[i];
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
		
		cout<<"Please Choose What to Delete: \n1.Delete Data of Specific Employee \n2.Delete Everything \n3.Exit \nEnter Option: ";
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
	
	cout<<"\n\nEnter the ID of the Employee: ";
	cin>>d;
	
	for(int i = 0; i < total; i++)
	{
		if(sw == true)
		{
			name[i] = name[i + 1];
			address[i] = address[i + 1];
			DoB[i] = DoB[i + 1];
			id[i] = id[i + 1];
			DoJ[i] = DoJ[i + 1];
			m_num[i] = m_num[i + 1];
			email[i] = email[i + 1];
		}
		
		if(d == id[i])
		{
			cout<<"\n\nData of Employee "<< i + 1;
						
			cout<<"\n\n\n  ** PERSONAL DETAILS **\n\n";
			cout<<"Name: "<<name[i]<<"\n";
			cout<<"Address: "<<address[i]<<"\n";
			cout<<"Date of Birth: "<<DoB[i]<<"\n\n\n";
			
			cout<<"  ** WORK DETAILS **\n\n";
			cout<<"ID: "<<id[i]<<"\n";
			cout<<"Date of Joining: "<<DoJ[i]<<"\n\n\n";
	
			cout<<"  ** CONTACT DETAILS **\n\n";
			cout<<"Mobile Number: "<<m_num[i]<<"\n";
			cout<<"Email ID: "<<email[i]<<"\n\n\n";
			
			cout<<"Do you want to Delete Data about this employee [Y/N]: ";
			cin>>op;
		}
		
		if(op == 'y' || op =='Y');
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
