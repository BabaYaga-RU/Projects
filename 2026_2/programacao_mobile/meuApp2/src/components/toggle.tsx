import { useState} from "react"
import {View, Text, StyleSheet, Pressable} from 'react-native'

export default function ToggleSimples(){
  const [ligado, setlLigado] = useState<boolean>(false)
  return(
    <View style={styles.container}>
        <Text style={styles.status}>
          {ligado ? 'ligado' : 'Desligado'}
        </Text>
        <Pressable
          OnPress={()=>setlLigado((prev =>!prev)}
          style={ligado ? styles.botaoLigado:styles.botaoDesligado}
        >
          <Text style={styles.textoBotao}>
            {ligado ? 'Ligado' : 'Desligado'}
          </Text>
        </Pressable>
    </View>
  )
}
const styles = StyleSheet.create({
  container:{
    flex:1,
    justifyContent:"center",
    alignItems:"center",
    gap:10
  },
  status:{},
  botaoLigado:{},
  botaoDesligado:{}
})