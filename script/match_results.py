from wrangler import dw
import sys

if(len(sys.argv) < 3):
	sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Split data repeatedly on newline  into  rows
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="\n",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Split data repeatedly on 'tab'
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on="\t",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Split split4 on '-'
w.add(dw.Split(column=["split4"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on="-",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=1,
               positions=None,
               quote_character=None))

# Split split6 between '  any word ' and ' any number '
w.add(dw.Split(column=["split6"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on=".*",
               before="\\d+",
               after=" [a-zA-Z]+",
               ignore_between=None,
               which=1,
               max=1,
               positions=None,
               quote_character=None))

# Edit split5  rows where split5 = 'FCZ '  to ' 1 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="FCZ ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="1",
              update_method=None))

# Edit split7  rows where split7 = ' FCZ'  to ' 1 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" FCZ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="1",
              update_method=None))

# Edit split5  rows where split5 = 'St. Gallen '  to ' 12 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="St. Gallen ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="12",
              update_method=None))

# Edit split7  rows where split7 = ' St'  to ' 12 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" St",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="12",
              update_method=None))

# Edit split5  rows where split5 = 'Young Boys '  to ' 9 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Young Boys ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="9",
              update_method=None))

# Edit split7  rows where split7 = ' Young'  to ' 9 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Young",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="9",
              update_method=None))

# Edit split7  rows where split7 = ' Thun'  to ' 10 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Thun",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="10",
              update_method=None))

# Edit split5  rows where split5 = 'Thun '  to ' 10 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Thun ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="10",
              update_method=None))

# Edit split5  rows where split5 = 'Basel '  to ' 11 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Basel ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="11",
              update_method=None))

# Edit split7  rows where split7 = ' Basel'  to ' 11 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Basel",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="11",
              update_method=None))

# Edit split7  rows where split7 = ' Grasshoppers'  to ' 13 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Grasshoppers",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="13",
              update_method=None))

# Edit split5  rows where split5 = 'Grasshoppers '  to ' 13 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Grasshoppers ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="13",
              update_method=None))

# Edit split5  rows where split5 = 'Schaffhausen '  to ' 14 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Schaffhausen ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="14",
              update_method=None))

# Edit split7  rows where split7 = ' Schaffhausen'  to ' 14 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Schaffhausen",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="14",
              update_method=None))

# Edit split7  rows where split7 = ' Neuch'  to ' 15 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Neuch",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="15",
              update_method=None))

# Edit split5  rows where split5 = 'Neuchâtel Xamax '  to ' 15 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Neuchâtel Xamax ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="15",
              update_method=None))

# Edit split7  rows where split7 = ' Yverdon'  to ' 16 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Yverdon",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="16",
              update_method=None))

# Edit split5  rows where split5 = 'Yverdon '  to ' 16 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Yverdon ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="16",
              update_method=None))

# Edit split7  rows where split7 = ' Aarau'  to ' 17 '
w.add(dw.Edit(column=["split7"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split7",
            value=" Aarau",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="17",
              update_method=None))

# Edit split5  rows where split5 = 'Aarau '  to ' 17 '
w.add(dw.Edit(column=["split5"],
              table=0,
              status="active",
              drop=False,
              result="column",
              update=True,
              insert_position="right",
              row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.Eq(column=[],
            table=0,
            status="active",
            drop=False,
            lcol="split5",
            value="Aarau ",
            op_str="=")]),
              on=None,
              before=None,
              after=None,
              ignore_between=None,
              which=1,
              max=1,
              positions=None,
              to="17",
              update_method=None))

# Drop split1
w.add(dw.Drop(column=["split1"],
              table=0,
              status="active",
              drop=True))

# Drop split3
w.add(dw.Drop(column=["split3"],
              table=0,
              status="active",
              drop=True))

# Split split8 on ':'
w.add(dw.Split(column=["split8"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on=":",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=1,
               positions=None,
               quote_character=None))

# Set  split  name to  date
w.add(dw.SetName(column=["split"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["date"],
                 header_row=None))

# Drop split2
w.add(dw.Drop(column=["split2"],
              table=0,
              status="active",
              drop=True))

# Set  split5  name to  team_home
w.add(dw.SetName(column=["split5"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["team_home"],
                 header_row=None))

# Set  split7  name to  team_away
w.add(dw.SetName(column=["split7"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["team_away"],
                 header_row=None))

# Set  split9  name to  goals_home
w.add(dw.SetName(column=["split9"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["goals_home"],
                 header_row=None))

# Set  split10  name to  goals_away
w.add(dw.SetName(column=["split10"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["goals_away"],
                 header_row=None))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

