import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model("/Git/dynamic-follow-tf/dynamic_follow_model")
#prediction=model.predict(np.asarray([[[31., 60., 22]]]))
#print(prediction)
print(model.predict(np.asarray([[[20.706933975219727, 58.459999084472656, 19.756933212280273], [20.725059509277344, 58.31999969482422, 19.768638610839844], [20.778053283691406, 58.08000183105469, 19.840553283691406], [20.788375854492188, 58.08000183105469, 19.838375091552734], [20.816028594970703, 57.91999816894531, 19.85352897644043], [20.826984405517578, 57.97999954223633, 19.84528160095215], [20.856098175048828, 58.040000915527344, 19.86623191833496], [20.883346557617188, 57.97999954223633, 19.826343536376953], [20.900148391723633, 57.86000061035156, 19.862648010253906], [20.923526763916016, 58.50666809082031, 19.790193557739258], [20.938827514648438, 58.426666259765625, 19.830493927001953], [20.9812068939209, 57.7599983215332, 19.91323471069336], [20.994539260864258, 57.68000030517578, 19.87532615661621], [21.02470588684082, 57.63999938964844, 19.88129997253418], [21.037912368774414, 57.58000183105469, 19.869892120361328], [21.072277069091797, 57.540000915527344, 19.884777069091797], [21.08919906616211, 57.52000045776367, 19.889198303222656], [21.115402221679688, 57.41999816894531, 19.840402603149414], [21.14023780822754, 57.380001068115234, 19.820446014404297], [21.155439376831055, 57.279998779296875, 19.88042640686035], [21.177024841308594, 57.20000076293945, 19.90202522277832], [21.18589973449707, 57.18000030517578, 19.922840118408203], [21.21406364440918, 57.060001373291016, 19.907569885253906], [21.225753784179688, 57.0, 19.888254165649414], [21.254261016845703, 56.97999954223633, 19.879261016845703], [21.270509719848633, 56.86000061035156, 19.927600860595703], [21.29191780090332, 56.87999725341797, 19.905879974365234], [21.30864715576172, 56.900001525878906, 19.92877197265625], [21.320756912231445, 56.91999816894531, 19.920757293701172], [21.34439468383789, 56.779998779296875, 19.944395065307617], [21.354183197021484, 56.65999984741211, 19.929183959960938], [21.378923416137695, 57.36000061035156, 19.867816925048828], [21.38387680053711, 56.41999816894531, 19.921377182006836], [21.39997100830078, 56.29999923706055, 19.92679214477539], [21.41151237487793, 56.34000015258789, 19.858144760131836], [21.428197860717773, 56.279998779296875, 19.915935516357422], [21.44022560119629, 56.119998931884766, 19.848093032836914], [21.448013305664062, 55.86000061035156, 19.835100173950195], [21.465747833251953, 55.73999786376953, 19.824312210083008], [21.47085189819336, 55.65999984741211, 19.803373336791992], [21.48774528503418, 55.720001220703125, 19.812746047973633], [21.49519157409668, 55.880001068115234, 19.816082000732422], [21.50415802001953, 55.73999786376953, 19.8427734375], [21.512271881103516, 55.65999984741211, 19.82042694091797], [21.517372131347656, 55.52000045776367, 19.742372512817383], [21.53331756591797, 55.380001068115234, 19.800081253051758], [21.53725242614746, 55.36000061035156, 19.73564338684082], [21.545738220214844, 55.18000030517578, 19.733238220214844], [21.54204559326172, 55.060001373291016, 19.70284080505371], [21.56076431274414, 54.959999084472656, 19.757863998413086], [21.560752868652344, 54.880001068115234, 19.783597946166992], [21.570241928100586, 54.86000061035156, 19.83274269104004], [21.573646545410156, 54.65999984741211, 19.83614730834961], [21.57862663269043, 54.540000915527344, 19.841127395629883], [21.598299026489258, 54.41999816894531, 19.808067321777344], [21.59071922302246, 54.36000061035156, 19.753219604492188], [21.607282638549805, 54.34000015258789, 19.74173927307129], [21.600696563720703, 54.2400016784668, 19.711917877197266], [21.612638473510742, 54.02000045776367, 19.71314811706543], [21.618253707885742, 53.939998626708984, 19.680753707885742], [21.625852584838867, 53.86000061035156, 19.702106475830078], [21.638965606689453, 53.70000076293945, 19.701465606689453], [21.638057708740234, 53.58000183105469, 19.700557708740234], [21.6597843170166, 53.5, 19.719482421875], [21.667133331298828, 53.400001525878906, 19.66042137145996], [21.677701950073242, 53.31999969482422, 19.63943099975586], [21.688817977905273, 53.20000076293945, 19.688817977905273], [21.69978141784668, 53.119998931884766, 19.713045120239258], [21.710432052612305, 52.939998626708984, 19.745935440063477], [21.709226608276367, 52.84000015258789, 19.759225845336914], [21.731874465942383, 52.73999786376953, 19.777631759643555], [21.73625373840332, 52.63999938964844, 19.72308921813965], [21.761606216430664, 52.58000183105469, 19.72222328186035], [21.772294998168945, 52.540000915527344, 19.709794998168945], [21.7886905670166, 52.41999816894531, 19.751190185546875], [21.806297302246094, 52.36000061035156, 19.78129768371582], [21.81247329711914, 52.380001068115234, 19.762474060058594], [21.839017868041992, 52.26000213623047, 19.77130699157715], [21.85402488708496, 52.13999938964844, 19.75151824951172], [21.86024284362793, 52.02000045776367, 19.809078216552734], [21.868127822875977, 51.880001068115234, 19.776309967041016], [21.879247665405273, 51.76000213623047, 19.791540145874023], [21.881629943847656, 51.63999938964844, 19.84412956237793], [21.881643295288086, 51.560001373291016, 19.871322631835938], [21.90143585205078, 51.459999084472656, 19.849002838134766], [21.90411376953125, 51.380001068115234, 19.839372634887695], [21.905059814453125, 51.31999969482422, 19.80829620361328], [21.905242919921875, 51.15999984741211, 19.789743423461914], [21.91703224182129, 51.040000915527344, 19.789215087890625], [21.923795700073242, 50.959999084472656, 19.79513931274414], [21.927989959716797, 50.86000061035156, 19.86710548400879], [21.9388484954834, 50.720001220703125, 19.850862503051758], [21.934986114501953, 50.619998931884766, 19.846872329711914], [21.93926429748535, 50.47999954223633, 19.902833938598633], [21.94047737121582, 50.34000015258789, 19.877233505249023], [21.94428253173828, 50.2400016784668, 19.88113784790039], [21.95175552368164, 50.18000030517578, 19.864255905151367], [21.945322036743164, 50.08000183105469, 19.92032241821289], [21.949100494384766, 49.959999084472656, 19.88682746887207], [21.953725814819336, 49.86000061035156, 19.8751163482666], [21.949399948120117, 49.720001220703125, 19.927248001098633], [21.946910858154297, 49.58000183105469, 19.8823184967041], [21.950237274169922, 49.47999954223633, 19.902368545532227], [21.959197998046875, 49.36000061035156, 19.94165802001953], [21.950061798095703, 49.279998779296875, 19.966266632080078], [21.947681427001953, 49.15999984741211, 19.9351806640625], [21.942276000976562, 49.060001373291016, 19.91327667236328], [21.939289093017578, 49.02000045776367, 19.88928985595703], [21.926279067993164, 48.91999816894531, 19.926279067993164], [21.924781799316406, 48.880001068115234, 19.95334815979004], [21.925640106201172, 48.73999786376953, 19.924345016479492], [21.90937042236328, 48.58000183105469, 19.975006103515625], [21.91193962097168, 48.52000045776367, 19.989152908325195], [21.906269073486328, 48.44000244140625, 20.00535774230957], [21.90094757080078, 48.29999923706055, 20.016504287719727], [21.893295288085938, 48.20000076293945, 20.00450325012207], [21.88933753967285, 48.53333282470703, 20.007522583007812], [21.886716842651367, 48.46666717529297, 20.012569427490234], [21.88392448425293, 48.413333892822266, 19.958925247192383], [21.877986907958984, 48.3466682434082, 19.969654083251953], [21.86674690246582, 48.22666549682617, 19.976682662963867], [21.866086959838867, 48.37333297729492, 20.033954620361328], [21.85874366760254, 48.38666534423828, 20.050792694091797], [21.8554630279541, 48.30666732788086, 20.12347984313965], [21.852190017700195, 48.21333312988281, 20.09416389465332], [21.84640884399414, 47.380001068115234, 20.061307907104492], [21.834918975830078, 47.619998931884766, 20.122419357299805], [21.82465362548828, 47.36000061035156, 20.151077270507812], [21.823177337646484, 47.119998931884766, 20.098176956176758], [21.81598472595215, 46.939998626708984, 20.12848472595215], [21.808652877807617, 46.84000015258789, 20.122400283813477], [21.807266235351562, 46.880001068115234, 20.156787872314453], [21.79494857788086, 46.84000015258789, 20.135496139526367], [21.78818130493164, 46.779998779296875, 20.125680923461914], [21.777713775634766, 46.73999786376953, 20.117467880249023], [21.774625778198242, 46.720001220703125, 20.12462615966797], [21.769947052001953, 46.63999938964844, 20.1324462890625], [21.769168853759766, 46.459999084472656, 20.119169235229492], [21.764728546142578, 46.29999923706055, 20.1898193359375], [21.762332916259766, 46.220001220703125, 20.212873458862305], [21.760562896728516, 46.099998474121094, 20.198062896728516], [21.761825561523438, 46.040000915527344, 20.186824798583984], [21.76318359375, 46.0, 20.163183212280273], [21.767074584960938, 45.939998626708984, 20.15457534790039], [21.77311897277832, 45.880001068115234, 20.207582473754883], [21.77554702758789, 45.81999969482422, 20.236940383911133], [21.77251434326172, 45.79999923706055, 20.29926872253418], [21.777841567993164, 45.79999923706055, 20.375411987304688], [21.777584075927734, 45.5, 20.290084838867188], [21.788494110107422, 45.31999969482422, 20.26349449157715]]])))